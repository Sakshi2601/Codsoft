import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactApp:
    def __init__(self):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x200")
        self.root.config(bg="#f0f0f0")

        self.contacts = []

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        title_label = tk.Label(self.root, text="Contact Book", font=("Arial", 16), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # Add Contact Button
        add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="white", padx=10, pady=5)
        add_button.grid(row=0, column=0, padx=10)

        # View Contact List Button
        view_button = tk.Button(button_frame, text="View Contact List", command=self.view_contacts, bg="#008CBA", fg="white", padx=10, pady=5)
        view_button.grid(row=0, column=1, padx=10)

        # Search Contact Button
        search_button = tk.Button(button_frame, text="Search Contact", command=self.search_contact, bg="#f44336", fg="white", padx=10, pady=5)
        search_button.grid(row=0, column=2, padx=10)

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter contact name:")
        phone = simpledialog.askstring("Phone", "Enter contact phone:")
        email = simpledialog.askstring("Email", "Enter contact email:")
        address = simpledialog.askstring("Address", "Enter contact address:")
        
        if name and phone and email and address:
            self.contacts.append(Contact(name, phone, email, address))
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please provide all details.")

    def view_contacts(self):
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("Contact List")
        contacts_window.geometry("700x250")

        tree = ttk.Treeview(contacts_window, columns=("Name", "Phone", "Email", "Address"), show='headings')
        tree.heading("Name", text="Name")
        tree.heading("Phone", text="Phone")
        tree.heading("Email", text="Email")
        tree.heading("Address", text="Address")

        tree.column("Name", width=150)
        tree.column("Phone", width=100)
        tree.column("Email", width=200)
        tree.column("Address", width=250)

        for contact in self.contacts:
            tree.insert("", "end", values=(contact.name, contact.phone, contact.email, contact.address))

        tree.pack(pady=10, padx=10)

        # Add a right-click menu for editing and deleting
        menu = tk.Menu(contacts_window, tearoff=0)
        menu.add_command(label="Update", command=lambda: self.update_contact(tree))
        menu.add_command(label="Delete", command=lambda: self.delete_contact(tree))
        
        def on_right_click(event):
            item = tree.identify_row(event.y)
            if item:
                tree.selection_set(item)
                menu.post(event.x_root, event.y_root)

        tree.bind("<Button-3>", on_right_click)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        results_window = tk.Toplevel(self.root)
        results_window.title("Search Results")
        results_window.geometry("700x300")

        tree = ttk.Treeview(results_window, columns=("Name", "Phone", "Email", "Address"), show='headings')
        tree.heading("Name", text="Name")
        tree.heading("Phone", text="Phone")
        tree.heading("Email", text="Email")
        tree.heading("Address", text="Address")

        tree.column("Name", width=150)
        tree.column("Phone", width=100)
        tree.column("Email", width=200)
        tree.column("Address", width=250)
        
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                tree.insert("", "end", values=(contact.name, contact.phone, contact.email, contact.address))

        tree.pack(pady=10, padx=10)

    def update_contact(self, tree):
        selected_item = tree.selection()[0]
        contact_info = tree.item(selected_item, 'values')
        
        contact = next((c for c in self.contacts if c.name == contact_info[0] and c.phone == contact_info[1]), None)
        
        if contact:
            name = simpledialog.askstring("Update Name", "Enter new contact name:", initialvalue=contact.name)
            phone = simpledialog.askstring("Update Phone", "Enter new contact phone:", initialvalue=contact.phone)
            email = simpledialog.askstring("Update Email", "Enter new contact email:", initialvalue=contact.email)
            address = simpledialog.askstring("Update Address", "Enter new contact address:", initialvalue=contact.address)
            
            if name and phone and email and address:
                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address
                messagebox.showinfo("Success", "Contact updated successfully!")
                tree.item(selected_item, values=(contact.name, contact.phone, contact.email, contact.address))
            else:
                messagebox.showwarning("Input Error", "Please provide all details.")

    def delete_contact(self, tree):
        selected_item = tree.selection()[0]
        contact_info = tree.item(selected_item, 'values')
        
        contact = next((c for c in self.contacts if c.name == contact_info[0] and c.phone == contact_info[1]), None)
        
        if contact:
            self.contacts.remove(contact)
            tree.delete(selected_item)
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp()
    root.mainloop()