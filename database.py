import sqlite3
from datetime import datetime

DB_PATH = "invoices.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id          TEXT PRIMARY KEY,
            client_name TEXT NOT NULL,
            total       REAL NOT NULL,
            filename    TEXT NOT NULL,
            created_at  TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Initialized invoices.db")

def save_invoice(invoice_id, client_name, total, filename):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO invoices VALUES (?,?,?,?,?)",
        (invoice_id, client_name, total, filename,
         datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def get_all_invoices():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT * FROM invoices ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return rows
