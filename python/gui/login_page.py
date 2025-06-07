import tkinter as tk
from tkinter import messagebox
from core.user_auth import login_user
from gui.register_page import open_register_page
from gui.selection_page import open_selection_page

def create_button(master, text, command):
    btn = tk.Label(master, text=text, bg="#000000", fg="#ffffff", font=("Arial", 11), padx=20, pady=10, cursor="hand2", bd=0)
    btn.bind("<Button-1>", lambda e: command())
    return btn

def open_login_page(root):
    root.title("SmartBeauty - Login")
    root.geometry("500x400")
    root.configure(bg="#ffdce5") 

    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg="#ffdce5")
    frame.pack(expand=True)

    tk.Label(frame, text="Login", font=("Arial", 20, "bold"), bg="#ffdce5", fg="black").pack(pady=10)

    tk.Label(frame, text="Username", bg="#ffdce5", fg="black", font=("Arial", 12)).pack()
    entry_username = tk.Entry(frame)
    entry_username.pack()

    tk.Label(frame, text="Password", bg="#ffdce5", fg="black", font=("Arial", 12)).pack()
    entry_password = tk.Entry(frame, show="*")
    entry_password.pack()

    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        if login_user(username, password):
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            open_selection_page(root, username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    create_button(frame, "Login", handle_login).pack(pady=10)
    create_button(frame, "Register", lambda: open_register_page(root)).pack()

