import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class ClientVibe:
    def __init__(self, master):
        master.title("ClientVibe")
        master.geometry("400x300")

        ttk.Label(master, text="Add New Client", font=("Roboto", 14, "bold")).pack(pady=5)

        ttk.Label(master, text="Name:", font=("Roboto", 12, "normal")).pack(pady=5)
        self.entry_name = ttk.Entry(master, font=("Roboto", 10, "normal"))
        self.entry_name.pack(pady=5)

        ttk.Label(master, text="Phone Number:", font=("Roboto", 12, "normal")).pack(pady=5)
        self.entry_phone = ttk.Entry(master, font=("Roboto", 10, "normal"))
        self.entry_phone.pack(pady=5)

        ttk.Label(master, text="Email:", font=("Roboto", 12, "normal")).pack(pady=5)
        self.entry_email = ttk.Entry(master, font=("Roboto", 10, "normal"))
        self.entry_email.pack(pady=5)

        ttk.Button(master, text="ADD", command=self.add_client).pack(pady=5)
        ttk.Style().configure("TButton", font=("Roboto", 10, "normal"))

    def validate_phone(self, phone):
        pattern = r"^\d{10}$"
        return re.match(pattern, phone)

    def validate_email(self, email):
        pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        return re.match(pattern, email)

    def add_client(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()

        if not name or not phone_number or not email:
            messagebox.showerror("Error", message="Please fill all the fields")
            return
        if not self.validate_phone(phone_number):
            messagebox.showerror("Error", message="Please Enter valid phone number")
            return
        if not self.validate_email(email):
            messagebox.showerror("Error", message="Please Enter valid email")
            return

        messagebox.showinfo("Success", "Client successfully added!")
        print(name)
        print(phone_number)
        print(email)



root = tk.Tk()
app = ClientVibe(root)
root.mainloop()
