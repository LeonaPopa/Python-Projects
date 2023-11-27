import tkinter as tk
from tkinter import ttk
import string
import secrets

def on_generate():
    length = int(var_length.get())
    include_uppercase = var_uppercase.get() == 1
    include_lowercase = var_lowercase.get() == 1
    include_numbers = var_numbers.get() == 1
    include_symbols = var_symbols.get() == 1

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
    label_password['text'] = password

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    # Define the character set based on the user's options
    char_set = ""
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_lowercase:
        char_set += string.ascii_lowercase
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation

    # Generate a password using the secrets library
    password = ''.join(secrets.choice(char_set) for i in range(length))
    return password


root = tk.Tk()
root.title("Password Generator")


var_length = tk.IntVar(value=12)
var_uppercase = tk.IntVar(value=1)
var_lowercase = tk.IntVar(value=1)
var_numbers = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=1)

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_length = ttk.Label(frame, text="Length:")
label_length.grid(row=0, column=0, sticky=tk.W)

spinbox_length = ttk.Spinbox(frame, from_=1, to=100, textvariable=var_length)
spinbox_length.grid(row=0, column=1)

label_uppercase = ttk.Checkbutton(frame, text="Uppercase", variable=var_uppercase)
label_uppercase.grid(row=1, column=0, columnspan=2, sticky=tk.W)

label_lowercase = ttk.Checkbutton(frame, text="Lowercase", variable=var_lowercase)
label_lowercase.grid(row=2, column=0, columnspan=2, sticky=tk.W)

label_numbers = ttk.Checkbutton(frame, text="Numbers", variable=var_numbers)
label_numbers.grid(row=3, column=0, columnspan=2, sticky=tk.W)

label_symbols = ttk.Checkbutton(frame, text="Symbols", variable=var_symbols)
label_symbols.grid(row=4, column=0, columnspan=2, sticky=tk.W)

button_generate = ttk.Button(frame, text="Generate", command=on_generate)
button_generate.grid(row=5, column=0, columnspan=2)

label_password = ttk.Label(frame, text="")
label_password.grid(row=6, column=0, columnspan=2, pady=10)


root.mainloop()