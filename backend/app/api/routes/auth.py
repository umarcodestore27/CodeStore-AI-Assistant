import psycopg2
import hashlib


from backend.app.db.db import get_connection
def signup(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed)
        )
        conn.commit()
        return True
    except:
        return False

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = hashlib.sha256(password.encode()).hexdigest()

    print("Entered password:", password)
    print("Generated hash:", hashed)

    cursor.execute("SELECT username, password FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    print("DB value:", user)

    if user:
        return hashed == user[1]

    return False