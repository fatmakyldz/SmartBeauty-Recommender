import sqlite3
import os
import hashlib

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.db')

def hash_password(password):
    """Returns a hashed version of the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    """Creates the users table if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def register_user(username, password, confirm_password):
    """Registers a new user with validation. Returns (success: bool, message: str)."""

    if not username or not password or not confirm_password:
        return False, "Please fill in all fields."

    if password != confirm_password:
        return False, "Passwords do not match."

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return False, "This username is already registered."

    hashed = hash_password(password)
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
        return True, "Registration successful!"
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"

def login_user(username, password):
    """Validates user login. Returns True if credentials are correct."""
    hashed = hash_password(password)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed))
        return cursor.fetchone() is not None
