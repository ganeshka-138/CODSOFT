import tkinter as tk 
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x600")
        self.root.configure(bg="#ECEFF1")

        self.contacts = {}

        self.title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 24, "bold"), bg="#546E7A", fg="#FFFFFF", bd=10, relief="groove", padx=20, pady=10)
        self.title_label.pack(pady=20)

        self.form_frame = tk.Frame(root, bg="#ECEFF1", bd=2, relief="groove")
        self.form_frame.pack(pady=20, padx=20, fill="x")

        self.name_label = tk.Label(self.form_frame, text="Name:", bg="#ECEFF1", fg="#37474F", font=("Helvetica", 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.form_frame, bd=2, relief="solid", font=("Helvetica", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(self.form_frame, text="Phone Number:", bg="#ECEFF1", fg="#37474F", font=("Helvetica", 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = tk.Entry(self.form_frame, bd=2, relief="solid", font=("Helvetica", 12), width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = tk.Label(self.form_frame, text="Email:", bg="#ECEFF1", fg="#37474F", font=("Helvetica", 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = tk.Entry(self.form_frame, bd=2, relief="solid", font=("Helvetica", 12), width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = tk.Label(self.form_frame, text="Address:", bg="#ECEFF1", fg="#37474F", font=("Helvetica", 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.address_entry = tk.Entry(self.form_frame, bd=2, relief="solid", font=("Helvetica", 12), width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.button_frame = tk.Frame(root, bg="#ECEFF1")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, bg="#66BB6A", fg="#FFFFFF", font=("Helvetica", 12, "bold"), bd=3, relief="raised", width=15)
        self.add_button.grid(row=0, column=0, padx=10, pady=10)

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts, bg="#42A5F5", fg="#FFFFFF", font=("Helvetica", 12, "bold"), bd=3, relief="raised", width=15)
        self.view_button.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, bg="#FFCA28", fg="#FFFFFF", font=("Helvetica", 12, "bold"), bd=3, relief="raised", width=15)
        self.search_button.grid(row=1, column=0, padx=10, pady=10)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, bg="#FFA726", fg="#FFFFFF", font=("Helvetica", 12, "bold"), bd=3, relief="raised", width=15)
        self.update_button.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, bg="#EF5350", fg="#FFFFFF", font=("Helvetica", 12, "bold"), bd=3, relief="raised", width=32)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone Number are required.")

    def view_contacts(self):
        contact_list = "\n".join([f"{name}: {info['phone']}" for name, info in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list if contact_list else "No contacts available.")

    def search_contact(self):
        name = simpledialog.askstring("Search", "Enter the name or phone number:")
        contact = self.contacts.get(name)
        if contact:
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        if name in self.contacts:
            phone = simpledialog.askstring("Update Phone", "Enter new phone number:")
            email = simpledialog.askstring("Update Email", "Enter new email:")
            address = simpledialog.askstring("Update Address", "Enter new address:")
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
