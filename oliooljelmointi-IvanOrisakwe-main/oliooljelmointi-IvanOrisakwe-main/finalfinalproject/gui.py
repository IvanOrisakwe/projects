import tkinter as tk
from tkinter import messagebox
from database import DB
from user import User

class UserInterface:
    """
    GUI for managing bank users.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Bank User Manager")

        self.db = DB()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()
        self.assets_entry = tk.Entry(root)
        self.assets_entry.pack()

        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        tk.OptionMenu(root, self.gender_var, "Male", "Female", "Other").pack()

        tk.Button(root, text="Add User", command=self.add_user).pack()
        tk.Button(root, text="Delete Selected", command=self.delete_selected).pack()

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack()
        self.update_list()

    def add_user(self):
        try:
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            assets = float(self.assets_entry.get())
            gender = self.gender_var.get()

            user = User(name, age, gender, assets)
            self.db.insert_user(user)
            self.update_list()
        except ValueError:
            messagebox.showerror("Invalid input", "Please check age and assets format.")

    def delete_selected(self):
        try:
            selection = self.listbox.curselection()
            if selection:
                item = self.listbox.get(selection[0])
                user_id = int(item.split(",")[0])  # ID is first column
                self.db.delete_user(user_id)
                self.update_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for user in self.db.fetch_users():
            self.listbox.insert(tk.END, f"{user[0]}, {user[1]}, {user[2]}, {user[3]}, {user[4]}€")
