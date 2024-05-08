import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import database


class Clients:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def create(self):
        cursor = database.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS clientVibe")
        cursor.execute("USE clientVibe")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS clients(name VARCHAR(100) NOT NULL, phone_number CHAR(10) NOT NULL, email VARCHAR(100) NOT NULL)")
        cursor.execute("INSERT INTO clients VALUES(%s,%s,%s)", (self.name, self.phone_number, self.email), )
        database.connection.commit()
        cursor.close()

    @staticmethod
    def fetch_all():
        cursor = database.connection.cursor()
        cursor.execute("USE clientVibe")
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()
        cursor.close()
        return clients


class ClientVibe:
    def __init__(self, master):
        self.master = master
        self.master.title("ClientVibe")
        self.master.geometry("400x300")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both')

        self.add_client_tab()
        self.view_clients_tab()

    def add_client_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Add Client')

        ttk.Label(frame, text="Add New Client", font=("Roboto", 14, "bold")).pack(pady=5)

        ttk.Label(frame, text="Name:", font=("Roboto", 12, "normal")).pack(pady=5)
        self.entry_name = ttk.Entry(frame, font=("Roboto", 10, "normal"))
        self.entry_name.pack(pady=5)

        ttk.Label(frame, text="Phone Number:", font=("Roboto", 12, "normal")).pack(pady=5)
        self.entry_phone = ttk.Entry(frame, font=("Roboto", 10, "normal"))
        self.entry_phone.pack(pady=5)

        ttk.Label(frame, text="Email:", font=("Roboto", 12, "normal")).pack(pady=5)
        self.entry_email = ttk.Entry(frame, font=("Roboto", 10, "normal"))
        self.entry_email.pack(pady=5)

        ttk.Button(frame, text="ADD", command=self.add_client).pack(pady=5)
        ttk.Style().configure("TButton", font=("Roboto", 10, "normal"))

    def view_clients_tab(self):
        # Create a frame for viewing clients
        view_clients_frame = ttk.Frame(self.notebook)
        view_clients_frame.pack(fill="both", padx=10, pady=10)

        # Create a Treeview widget to display client data in a tabular format
        self.treeview = ttk.Treeview(view_clients_frame, columns=("Name", "Phone Number", "Email"), show="headings")
        self.treeview.heading("Name", text="Name", anchor="center")
        self.treeview.heading("Phone Number", text="Phone Number", anchor="center")
        self.treeview.heading("Email", text="Email", anchor="center")
        self.treeview.pack(fill="both", expand=True)

        # Configure column widths to fit within the specified dimensions (400x300 pixels)
        self.treeview.column("Name", width=130)
        self.treeview.column("Phone Number", width=100)
        self.treeview.column("Email", width=150)

        # Populate the Treeview with client data
        clients = Clients.fetch_all()
        for client in clients:
            self.treeview.insert("", "end", values=client)

        # Add the frame to the notebook as a tab
        self.notebook.add(view_clients_frame, text="View Clients")

        # Apply styles to the Treeview widget
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Roboto", 10, "bold"))
        style.configure("Treeview", font=("Roboto", 10))

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

        client = Clients(name, phone_number, email)
        client.create()
        messagebox.showinfo("Success", "Client successfully added!")


root = tk.Tk()
app = ClientVibe(root)
root.mainloop()
