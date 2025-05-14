import sqlite3
from threading import Lock

db_lock = Lock()

# Database initialization
def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            price_range TEXT,
            median TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


# one line write function in applications
def insert_product(product):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, category, price_range, median, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        product.get("name"),
        product.get("category"),
        product.get("price_range"),
        product.get("median"),
        product.get("description")
    ))
    conn.commit()
    conn.close()

