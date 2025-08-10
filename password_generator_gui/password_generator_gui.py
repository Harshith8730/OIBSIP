import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            raise ValueError("Length should be at least 4")

        char_pool = ""
        if var_letters.get():
            char_pool += string.ascii_letters
        if var_numbers.get():
            char_pool += string.digits
        if var_symbols.get():
            char_pool += string.punctuation

        if not char_pool:
            raise ValueError("Select at least one character type")

        # Ensure one character from each selected type (security rule)
        password = []
        if var_letters.get():
            password.append(random.choice(string.ascii_letters))
        if var_numbers.get():
            password.append(random.choice(string.digits))
        if var_symbols.get():
            password.append(random.choice(string.punctuation))

        # Fill the rest of the password
        while len(password) < length:
            password.append(random.choice(char_pool))

        random.shuffle(password)
        final_password = "".join(password[:length])
        entry_result.delete(0, tk.END)
        entry_result.insert(0, final_password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    password = entry_result.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# GUI Design
app = tk.Tk()
app.title("Advanced Password Generator")
app.geometry("400x300")
app.config(bg="#e6f2ff")

tk.Label(app, text="Password Length:", bg="#e6f2ff").pack(pady=5)
entry_length = tk.Entry(app)
entry_length.pack()

# Options
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Letters", variable=var_letters, bg="#e6f2ff").pack()
tk.Checkbutton(app, text="Include Numbers", variable=var_numbers, bg="#e6f2ff").pack()
tk.Checkbutton(app, text="Include Symbols", variable=var_symbols, bg="#e6f2ff").pack()

# Generate Button
tk.Button(app, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

# Output Entry
entry_result = tk.Entry(app, font=("Arial", 12), justify="center")
entry_result.pack(pady=5)

# Copy Button
tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

app.mainloop()
