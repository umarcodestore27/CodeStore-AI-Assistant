from backend.app.db.db import get_connection

# Create chat
def create_chat(username, title="New Chat"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats (username, title) VALUES (%s, %s) RETURNING chat_id",
        (username, title)
    )

    chat_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return chat_id


# Get user chats
def get_user_chats(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT chat_id, title FROM chats WHERE username=%s ORDER BY created_at DESC",
        (username,)
    )

    chats = cursor.fetchall()
    cursor.close()
    conn.close()

    return chats


# Save message
def save_message(chat_id, role, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (chat_id, role, content) VALUES (%s, %s, %s)",
        (chat_id, role, content)
    )

    conn.commit()
    cursor.close()
    conn.close()


# Get messages
def get_chat_messages(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, content FROM messages WHERE chat_id=%s ORDER BY created_at",
        (chat_id,)
    )

    messages = cursor.fetchall()
    cursor.close()
    conn.close()

    return messages