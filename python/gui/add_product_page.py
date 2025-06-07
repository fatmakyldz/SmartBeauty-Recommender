import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

def open_add_product_page(window):
    window.title("SmartBeauty - Add New Product")
    window.geometry("600x750")
    window.configure(bg="#ffdce5")

    labels = [
        "Product Name", "Brand", "Category", "Skin Type (comma-separated)",
        "Usage Description", "Volume (ml)", "Price", "Product Link"
    ]
    
    entries = {}
    categories = ["Serum", "Moisturizer", "Toner", "Cleanser", "Mask", "Peeling", "Eye Care", "Lip Care"]

    for i, label in enumerate(labels):
        tk.Label(window, text=label + ":", bg="#ffdce5", fg="black", font=("Arial", 11)).pack(pady=(10 if i == 0 else 5, 2))

        if label == "Category":
            combo = ttk.Combobox(window, values=categories, state="readonly", font=("Arial", 11), width=42)
            combo.pack(pady=2)
            entries[label] = combo
        else:
            entry = tk.Entry(window, font=("Arial", 11), width=45)
            entry.pack(pady=2)
            entries[label] = entry

    def save_product():
        try:
            with open("data/products.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        try:
            new_id = max([item["id"] for item in data], default=0) + 1
        except:
            new_id = 1

        product = {
            "id": new_id,
            "name": entries["Product Name"].get(),
            "brand": entries["Brand"].get(),
            "category": entries["Category"].get(),
            "skin_type": [s.strip() for s in entries["Skin Type (comma-separated)"].get().split(",")],
            "usage": entries["Usage Description"].get(),
            "volume": entries["Volume (ml)"].get() + "ml",
            "price": float(entries["Price"].get()),
            "currency": "TRY",
        }

        if not all(str(v).strip() for v in product.values()):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            data.append(product)
            with open("data/products.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Success", "Product added successfully!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

    btn = tk.Label(window, text="Save Product", bg="#000000", fg="#ffffff", font=("Arial", 11), padx=20, pady=10, cursor="hand2", bd=0)
    btn.bind("<Button-1>", lambda e: save_product())
    btn.pack(pady=20)
