import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    if complexity == 'Low':
        characters = string.ascii_letters
        password = ''.join(secrets.choice(characters) for _ in range(length))
    elif complexity == 'Medium':
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(length))
        password = list(password)
        password[secrets.randbelow(length)] = secrets.choice(string.digits)
        password = ''.join(password)
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        password = list(password)
        password[secrets.randbelow(length)] = secrets.choice(string.ascii_letters)
        password[secrets.randbelow(length)] = secrets.choice(string.digits)
        password[secrets.randbelow(length)] = secrets.choice(string.punctuation)
        password = ''.join(password)
    return password

def evaluate_strength(password):
    length = len(password)
    categories = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ])
    if length >= 12 and categories >= 3:
        return "Strong"
    elif length >= 8 and categories >= 2:
        return "Medium"
    else:
        return "Weak"

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 6 or length > 128:
            raise ValueError
        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state='readonly')
        strength = evaluate_strength(password)
        strength_label.config(text=f"Strength: {strength}", fg="#27AE60" if strength == "Strong" else "#F1C40F" if strength == "Medium" else "#E74C3C")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid length between 6 and 128.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showerror("Error", "No password to copy.")

app = tk.Tk()
app.title("Password Generator")
app.geometry("450x500")
app.configure(bg="#1E1E2F")

title_label = tk.Label(app, text="Password Generator", font=("Helvetica", 20, "bold"), bg="#2C3E50", fg="#ECF0F1", padx=20, pady=10, relief="groove")
title_label.pack(pady=20)

length_frame = tk.Frame(app, bg="#1E1E2F")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", bg="#1E1E2F", fg="#FFFFFF", font=("Helvetica", 12))
length_label.pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, bd=2, relief="solid", font=("Helvetica", 12), width=10)
length_entry.pack(side=tk.LEFT, padx=5)
length_entry.insert(0, "12")

complexity_frame = tk.Frame(app, bg="#1E1E2F")
complexity_frame.pack(pady=10)
complexity_label = tk.Label(complexity_frame, text="Complexity:", bg="#1E1E2F", fg="#FFFFFF", font=("Helvetica", 12))
complexity_label.pack(side=tk.LEFT, padx=5)
complexity_var = tk.StringVar(value='Medium')
low_radio = tk.Radiobutton(complexity_frame, text='Low', variable=complexity_var, value='Low', bg="#1E1E2F", fg="#ECF0F1", selectcolor="#34495E", font=("Helvetica", 12))
low_radio.pack(side=tk.LEFT, padx=5)
medium_radio = tk.Radiobutton(complexity_frame, text='Medium', variable=complexity_var, value='Medium', bg="#1E1E2F", fg="#ECF0F1", selectcolor="#34495E", font=("Helvetica", 12))
medium_radio.pack(side=tk.LEFT, padx=5)
high_radio = tk.Radiobutton(complexity_frame, text='High', variable=complexity_var, value='High', bg="#1E1E2F", fg="#ECF0F1", selectcolor="#34495E", font=("Helvetica", 12))
high_radio.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(app, text="Generate Password", command=on_generate, bg="#E67E22", fg="#FFFFFF", font=("Helvetica", 14, "bold"), bd=5, relief="raised")
generate_button.pack(pady=20)

password_frame = tk.Frame(app, bg="#1E1E2F")
password_frame.pack(pady=10)
password_label = tk.Label(password_frame, text="Generated Password:", bg="#1E1E2F", fg="#FFFFFF", font=("Helvetica", 12))
password_label.pack(side=tk.LEFT, padx=5)
password_entry = tk.Entry(password_frame, bd=2, relief="solid", font=("Helvetica", 12), state='readonly', width=25)
password_entry.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(app, text="Copy Password", command=copy_to_clipboard, bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 12), bd=5, relief="raised")
copy_button.pack(pady=10)

strength_label = tk.Label(app, text="Strength: ", bg="#1E1E2F", fg="#ECF0F1", font=("Helvetica", 12))
strength_label.pack(pady=10)

app.mainloop()
