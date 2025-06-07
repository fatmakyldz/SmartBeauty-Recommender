import tkinter as tk
from tkinter import ttk
from gui.recommendation_page import open_recommendation_page
from gui.add_product_page import open_add_product_page

def create_button(master, text, command):
    btn = tk.Label(master, text=text, bg="#000000", fg="#ffffff", font=("Arial", 11), padx=20, pady=10, cursor="hand2", bd=0)
    btn.bind("<Button-1>", lambda e: command())
    return btn

def open_selection_page(root, username):
    root.title("SmartBeauty - Selection Page")  
    root.configure(bg="#ffdce5")  

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 14, "bold"), bg="#ffdce5", fg="black").pack(pady=10)

    tk.Label(root, text="Select skin sensitivity:", bg="#ffdce5", fg="black", font=("Arial", 12)).pack(pady=5)
    sensitivity_options = ["normal", "sensitive"]
    sensitivity_var = tk.StringVar()
    sensitivity_combo = ttk.Combobox(root, textvariable=sensitivity_var, values=sensitivity_options, state="readonly")
    sensitivity_combo.pack(pady=5)

    tk.Label(root, text="Select skin type:", bg="#ffdce5", fg="black", font=("Arial", 12)).pack(pady=5)
    skintype_options = ["dry", "oily", "combination"]
    skintype_var = tk.StringVar()
    skintype_combo = ttk.Combobox(root, textvariable=skintype_var, values=skintype_options, state="readonly")
    skintype_combo.pack(pady=5)

    tk.Label(root, text="Select category:", bg="#ffdce5", fg="black", font=("Arial", 12)).pack(pady=5)
    category_options = ["All", "Serum", "Moisturizer", "Toner", "Cleanser", "Mask", "Peeling", "Eye Care", "Lip Care"]
    category_var = tk.StringVar()
    category_combo = ttk.Combobox(root, textvariable=category_var, values=category_options, state="readonly")
    category_combo.pack(pady=5)

    def recommend():
        sensitivity = sensitivity_var.get()
        skintype = skintype_var.get()
        category = category_var.get()
        if not (sensitivity and skintype and category):
            tk.messagebox.showwarning("Input Error", "Please fill in all fields.")
            return
        open_recommendation_page(root, sensitivity, skintype, category, username)

    create_button(root, "Show Products", recommend).pack(pady=10)

    create_button(root, "Add New Product", lambda: open_add_product_page(tk.Toplevel(root))).pack(pady=10)
