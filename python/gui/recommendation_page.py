import tkinter as tk
from tkinter import ttk
import webbrowser
import platform
from core.recommend import recommend_products

def create_button(master, text, command, font_size=11):
    btn = tk.Label(master, text=text, bg="#000000", fg="#ffffff", font=("Arial", font_size), padx=20, pady=6, cursor="hand2", bd=0)
    btn.bind("<Button-1>", lambda e: command())
    return btn

def open_recommendation_page(root, sensitivity, skintype, category, username):
    root.title("SmartBeauty - Recommended Products")
    root.geometry("900x700")
    root.configure(bg="#ffdce5")

    for widget in root.winfo_children():
        widget.destroy()

    header_text = f"Recommended Products for: {sensitivity} & {skintype} skin"
    if category != "All":
        header_text += f" in {category}"

    tk.Label(root, text=header_text, font=("Arial", 14, "bold"), bg="#ffdce5", fg="black").pack(pady=10)

    canvas = tk.Canvas(root, height=500, bg="#ffdce5", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#ffdce5")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    products = recommend_products(sensitivity, skintype, None if category == "All" else category)

    if not products:
        tk.Label(scrollable_frame, text="No matching products found.", fg="red", bg="#ffdce5", font=("Arial", 11)).pack(pady=10)
    else:
        for product in products:
            frame = tk.Frame(scrollable_frame, bd=1, relief="solid", padx=10, pady=5, bg="white")
            frame.pack(padx=10, pady=5, fill="x")

            name = product.get("name", "Unnamed")
            brand = product.get("brand", "Unknown")
            price = product.get("price", "N/A")
            currency = product.get("currency", "TRY")
            volume = product.get("volume", "")
            usage = product.get("usage", "")
            link = product.get("link", "")

            tk.Label(frame, text=f"{name}", font=("Arial", 12, "bold"), bg="white", fg="black").pack(anchor="w")
            tk.Label(frame, text=f"Brand: {brand}", bg="white", fg="black", font=("Arial", 10)).pack(anchor="w")
            tk.Label(frame, text=f"Price: {price} {currency}   | Volume: {volume}", bg="white", fg="black", font=("Arial", 10)).pack(anchor="w")
            tk.Label(frame, text=f"Usage: {usage}", wraplength=600, justify="left", bg="white", fg="black", font=("Arial", 10)).pack(anchor="w", pady=3)

            if link:
                create_button(frame, "View Product", lambda url=link: webbrowser.open(url), font_size=10).pack(anchor="e", pady=5)

    def back_to_selection(current_window, username):
        from gui.selection_page import open_selection_page
        open_selection_page(current_window, username)

    create_button(root, "← Back", lambda: back_to_selection(root, username)).pack(pady=10)
