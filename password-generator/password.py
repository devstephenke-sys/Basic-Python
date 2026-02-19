import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())

        characters = string.ascii_letters

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        password = ""
        for _ in range(length):
            password += random.choice(characters)

        password_output.delete(0, tk.END)
        password_output.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


# Function to save password
def save_password():
    password = password_output.get()

    if password == "":
        messagebox.showwarning("Warning", "No password to save")
        return

    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    messagebox.showinfo("Saved", "Password saved successfully!")


# Create window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16)).pack(pady=10)

# Length input
tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Options
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output box
password_output = tk.Entry(root, width=30)
password_output.pack()

# Save button
tk.Button(root, text="Save Password", command=save_password).pack(pady=5)

root.mainloop()
