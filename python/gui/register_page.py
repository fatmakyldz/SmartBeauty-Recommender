import tkinter as tk
from tkinter import messagebox
from core.user_auth import register_user

def create_button(master, text, command):
    btn = tk.Label(master, text=text, bg="#000000", fg="#ffffff", font=("Arial", 11), padx=20, pady=10, cursor="hand2", bd=0)
    btn.bind("<Button-1>", lambda e: command())
    return btn

def open_register_page(window):
    window.destroy()

    register_window = tk.Tk()
    register_window.title("SmartBeauty - Register")
    register_window.geometry("500x400")
    register_window.configure(bg="#ffdce5")  

    frame = tk.Frame(register_window, bg="#ffdce5", padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text="Register", font=("Arial", 18, "bold"), bg="#ffdce5", fg="black").pack(pady=10)

    tk.Label(frame, text="Username", bg="#ffdce5", fg="black", font=("Arial", 12)).pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()

    tk.Label(frame, text="Password", bg="#ffdce5", fg="black", font=("Arial", 12)).pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack()

    tk.Label(frame, text="Confirm Password", bg="#ffdce5", fg="black", font=("Arial", 12)).pack()
    confirm_entry = tk.Entry(frame, show="*")
    confirm_entry.pack()

    def handle_register():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Password Error", "Passwords do not match.")
            return

        success, message = register_user(username, password, confirm_password)
        if success:
            messagebox.showinfo("Success", message)
            register_window.destroy()
            from gui.login_page import open_login_page
            open_login_page(tk.Tk())
        else:
            messagebox.showerror("Registration Failed", message)

    def back_to_login():
        register_window.destroy()
        from gui.login_page import open_login_page
        open_login_page(tk.Tk())

   
    create_button(frame, "Register", handle_register).pack(pady=10)
    create_button(frame, "← Back to Login", back_to_login).pack(pady=5)

    register_window.mainloop()
