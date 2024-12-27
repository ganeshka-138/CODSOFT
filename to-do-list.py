import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")
        self.root.configure(bg="#cce7ff")  # Full-page background color

        self.header = tk.Label(self.root, text="My To-Do List", font=("Helvetica", 24), bg="#cce7ff", fg="#003366")
        self.header.pack(pady=10)

        self.tasks = []

        self.frame = tk.Frame(self.root, bg="#cce7ff")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE, bg="#ffffff", fg="#000000")
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=52, bg="#e0e0e0", fg="#000000")
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#add8e6", font=("Helvetica", 12))
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task, bg="#90ee90", font=("Helvetica", 12))
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.remove_task, bg="#ff6347", font=("Helvetica", 12))
        self.delete_button.pack(pady=5)

        self.status_button = tk.Button(self.root, text="Toggle Status", command=self.toggle_status, bg="#ffa500", font=("Helvetica", 12))
        self.status_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append((task, "Pending"))
            self.refresh_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Edit Task", "Enter new task:", initialvalue=self.tasks[selected_index][0])
            if new_task:
                self.tasks[selected_index] = (new_task, self.tasks[selected_index][1])
                self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def toggle_status(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_index]
            new_status = "Completed" if current_task[1] == "Pending" else "Pending"
            self.tasks[selected_index] = (current_task[0], new_status)
            self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to toggle status.")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task, status in self.tasks:
            self.task_listbox.insert(tk.END, f"{task} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
