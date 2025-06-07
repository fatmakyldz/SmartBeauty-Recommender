import tkinter as tk
from core.user_auth import init_db
from gui.login_page import open_login_page

def main():
    init_db()

    root = tk.Tk()
    root.geometry("800x700")  
    root.resizable(False, False)  
    open_login_page(root)  
    root.mainloop()

if __name__ == "__main__":
    main()
