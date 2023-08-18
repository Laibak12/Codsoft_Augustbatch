import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []
        self.current_contact = None

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()

        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()

        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search Contacts", command=self.search_contacts)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and phone are required.")

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Contacts")

        for contact in self.contacts:
            contact_text = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n"
            contact_label = tk.Label(view_window, text=contact_text)
            contact_label.pack()

    def search_contacts(self):
        query = self.search_entry.get()
        results = []

        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                results.append(contact)

        if results:
            result_window = tk.Toplevel(self.root)
            result_window.title("Search Results")

            for contact in results:
                contact_text = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n"
                contact_label = tk.Label(result_window, text=contact_text)
                contact_label.pack()
        else:
            messagebox.showinfo("No Results", "No contacts found matching the search.")

    def update_contact(self):
        if self.current_contact:
            updated_name = self.name_entry.get()
            updated_phone = self.phone_entry.get()
            updated_email = self.email_entry.get()
            updated_address = self.address_entry.get()

            self.current_contact['name'] = updated_name
            self.current_contact['phone'] = updated_phone
            self.current_contact['email'] = updated_email
            self.current_contact['address'] = updated_address

            self.current_contact = None
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "No contact selected for update.")

    def delete_contact(self):
        if self.current_contact:
            self.contacts.remove(self.current_contact)
            self.current_contact = None
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "No contact selected for deletion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
