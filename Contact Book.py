import tkinter as tk
from tkinter import messagebox

contacts = {}
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        contact_listbox.insert(tk.END, name)
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

def view_contact(event):
    selected = contact_listbox.get(tk.ANCHOR)
    if selected in contacts:
        details = contacts[selected]
        details_var.set(f"Phone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")

def delete_contact():
    selected = contact_listbox.get(tk.ANCHOR)
    if selected in contacts:
        del contacts[selected]
        contact_listbox.delete(tk.ANCHOR)
        details_var.set("")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()

contact_listbox = tk.Listbox(root)
contact_listbox.pack()
contact_listbox.bind("<<ListboxSelect>>", view_contact)

details_var = tk.StringVar()
tk.Label(root, textvariable=details_var, font=("Arial", 12)).pack()

tk.Button(root, text="Delete Contact", command=delete_contact).pack()

root.mainloop()
