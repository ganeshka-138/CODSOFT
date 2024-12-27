import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x400")
        self.root.configure(bg="#e6f7ff")
        
        self.label = tk.Label(self.root, text="Simple Calculator", font=("Helvetica", 18, "bold"), bg="#0099cc", fg="#ffffff", bd=10, relief="solid", padx=20, pady=10)
        self.label.pack(pady=20)
        
        self.entry_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.entry_frame.pack(pady=10)
        
        self.number1_label = tk.Label(self.entry_frame, text="First Number:", bg="#e6f7ff", fg="#333333")
        self.number1_label.grid(row=0, column=0, padx=10, pady=5)
        self.number1_entry = tk.Entry(self.entry_frame, bd=5, relief="solid")
        self.number1_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.number2_label = tk.Label(self.entry_frame, text="Second Number:", bg="#e6f7ff", fg="#333333")
        self.number2_label.grid(row=1, column=0, padx=10, pady=5)
        self.number2_entry = tk.Entry(self.entry_frame, bd=5, relief="solid")
        self.number2_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.operation_label = tk.Label(self.entry_frame, text="Operation (+, -, *, /):", bg="#e6f7ff", fg="#333333")
        self.operation_label.grid(row=2, column=0, padx=10, pady=5)
        self.operation_entry = tk.Entry(self.entry_frame, bd=5, relief="solid")
        self.operation_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.button_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.button_frame.pack(pady=20)
        
        self.calculate_button = tk.Button(self.button_frame, text="Calculate", command=self.perform_calculation, bg="#0099cc", fg="#ffffff", font=("Helvetica", 12, "bold"), bd=5, relief="raised", padx=20, pady=10)
        self.calculate_button.grid(row=0, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_inputs, bg="#f44336", fg="#ffffff", font=("Helvetica", 12, "bold"), bd=5, relief="raised", padx=20, pady=10)
        self.clear_button.grid(row=0, column=1, padx=10, pady=10)

    def perform_calculation(self):
        try:
            number1 = float(self.number1_entry.get())
            number2 = float(self.number2_entry.get())
            operation = self.operation_entry.get()
            
            if operation == "+":
                result = number1 + number2
            elif operation == "-":
                result = number1 - number2
            elif operation == "*":
                result = number1 * number2
            elif operation == "/":
                if number2 != 0:
                    result = number1 / number2
                else:
                    messagebox.showwarning("Warning", "Cannot divide by zero.")
                    return
            else:
                messagebox.showwarning("Warning", "Invalid operation.")
                return
            
            messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter valid numbers.")

    def clear_inputs(self):
        self.number1_entry.delete(0, tk.END)
        self.number2_entry.delete(0, tk.END)
        self.operation_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
