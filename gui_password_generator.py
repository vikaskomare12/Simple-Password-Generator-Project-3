import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror(
                "Error",
                "Password length must be at least 4"
            )
            return

        characters = string.ascii_lowercase

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid password length"
        )


def copy_password():
    password = password_entry.get()

    if password:
        pyperclip.copy(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Include Uppercase Letters",
    variable=uppercase_var
).pack()

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=numbers_var
).pack()

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbols_var
).pack()

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password
)
generate_btn.pack(pady=10)

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
password_entry.pack()

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password
)
copy_btn.pack(pady=10)

root.mainloop()