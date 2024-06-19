import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate the password
def generate_password():
    length = length_var.get()
    
    if length.isdigit() and int(length) > 0:
        length = int(length)
        
        # Check for complexity options
        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        
        if not (use_upper or use_lower or use_digits or use_special):
            messagebox.showwarning("Warning", "Please select at least one character type")
            return
        
        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    else:
        messagebox.showerror("Error", "Please enter a valid number for length")

# Setting up the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="#ee6b6e")

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#ee6b6e")
title_label.pack(pady=10)

# Length Entry
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12), bg="#ee6b6e")
length_label.pack()
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, font=("Helvetica", 12))
length_entry.pack(pady=5)

# Checkbuttons for complexity options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

check_upper = tk.Checkbutton(root, text="Include Uppercase", variable=var_upper, font=("Helvetica", 12), bg="#ee6b6e")
check_upper.pack()
check_lower = tk.Checkbutton(root, text="Include Lowercase", variable=var_lower, font=("Helvetica", 12), bg="#ee6b6e")
check_lower.pack()
check_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits, font=("Helvetica", 12), bg="#ee6b6e")
check_digits.pack()
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, font=("Helvetica", 12), bg="#ee6b6e")
check_special.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg="darkblue", fg="white")
generate_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#ee6b6e")
result_label.pack()

# Run the application
root.mainloop()