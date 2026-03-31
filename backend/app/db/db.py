# import sqlite3

# conn = sqlite3.connect("chat.db", check_same_thread=False)
# c = conn.cursor()

# # USERS (already handled in auth, optional here)

# # CHATS TABLE
# c.execute("""
# CREATE TABLE IF NOT EXISTS chats (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT,
#     title TEXT
# )
# """)

# # MESSAGES TABLE
# c.execute("""
# CREATE TABLE IF NOT EXISTS messages (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     chat_id INTEGER,
#     role TEXT,
#     content TEXT
# )
# """)

# conn.commit()

# above one is using Sqlite,and the below is PostgreSQL

import psycopg2

def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        database="codestore_ai",
        user="postgres",
        password="Code@123"
    )