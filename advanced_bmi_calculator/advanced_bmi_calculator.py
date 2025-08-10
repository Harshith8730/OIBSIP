import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
import os

# CSV file to store history
DATA_FILE = "bmi_data.csv"

# Create file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        file.write("Name,Weight,Height,BMI,Category\n")

# BMI classification function
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Calculate BMI and store data
def calculate_bmi():
    try:
        name = entry_name.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = round(weight / (height ** 2), 2)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi} ({category})")

        # Save to CSV
        with open(DATA_FILE, "a") as file:
            file.write(f"{name},{weight},{height},{bmi},{category}\n")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Visualize data
def show_graph():
    try:
        df = pd.read_csv(DATA_FILE)
        if df.empty:
            messagebox.showinfo("No Data", "No historical data to show.")
            return

        plt.figure(figsize=(8,5))
        plt.hist(df["BMI"], bins=10, color='skyblue', edgecolor='black')
        plt.title("BMI Distribution")
        plt.xlabel("BMI Value")
        plt.ylabel("Number of Users")
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Could not show graph:\n{str(e)}")

# GUI Setup
app = tk.Tk()
app.title("Advanced BMI Calculator")
app.geometry("350x300")
app.config(bg="#f0f0f0")

tk.Label(app, text="Name:").pack(pady=3)
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Weight (kg):").pack(pady=3)
entry_weight = tk.Entry(app)
entry_weight.pack()

tk.Label(app, text="Height (m):").pack(pady=3)
entry_height = tk.Entry(app)
entry_height.pack()

tk.Button(app, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12), fg="blue")
result_label.pack()

tk.Button(app, text="View BMI Graph", command=show_graph, bg="#2196F3", fg="white").pack(pady=10)

app.mainloop()
