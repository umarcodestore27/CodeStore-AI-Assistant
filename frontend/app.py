import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from backend.app.services.ai_engine import ollama_chat
from backend.app.api.routes.auth import login, signup
from backend.app.services.chat_manager import (
create_chat,
get_user_chats,
save_message,
get_chat_messages
)
from backend.app.services.file_handler import extract_pdf_text, extract_code_text
import base64

st.set_page_config(page_title="CodeStore AI", layout="centered")

# ==============================
# SESSION STATE
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "user" not in st.session_state:
    st.session_state.user = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "chat_id" not in st.session_state:
    st.session_state.chat_id = None

# ==============================
# LOGIN UI
# ==============================
if not st.session_state.logged_in:

    try:
        logo_path = os.path.join(BASE_DIR, "frontend", "assets", "codestorelogo.webp")

        with open(logo_path, "rb") as f:
            logo = base64.b64encode(f.read()).decode()
    except:
        logo = ""

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="data:image/webp;base64,{logo}" width="140">
            <h1 style="font-size:42px;font-weight:700;margin-top:10px;">
            🔐 CodeStore AI Login
            </h1>
        </div>
        """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        username = st.text_input(
            "Username",
            key="login_user",
            placeholder="Enter username",
            help="",
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass",
            placeholder="Enter password",
        )

        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid credentials ❌")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Create Account"):
            if signup(new_user, new_pass):
                st.session_state.logged_in = True
                st.session_state.user = new_user
                st.success("Account created ✅ Logging you in...")
                st.rerun()
            else:
                st.error("User already exists ❌")

    st.info("👉 Default Login: admin / admin123")
    st.stop()
    st.session_state.chat_id = None
# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    logo_path = os.path.join(BASE_DIR, "frontend", "assets", "codestorelogo.webp")
    st.image(logo_path, width=200)

    st.markdown("### 💬 Chats")

    user_chats = get_user_chats(st.session_state.user) if st.session_state.user else []

    # Show chats
    for chat in user_chats:
        chat_id, title = chat
        title = title or "Untitled Chat"

        if st.button(title, key=f"chat_{chat_id}"):
            st.session_state.chat_id = chat_id
            st.session_state.messages = [
                {"role": role, "content": content}
                for role, content in get_chat_messages(chat_id)
            ]
            st.rerun()

    st.markdown("---")

    # Buttons (IMPORTANT)
    if st.button("➕ New Chat"):
        new_chat_id = create_chat(st.session_state.user, "New Chat")
        st.session_state.chat_id = new_chat_id
        st.session_state.messages = []
        st.session_state.uploaded_file = None
        st.rerun()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.uploaded_file = None
        st.rerun()

    st.markdown("📂 Upload File")

    uploaded_file = st.file_uploader(
        "Upload File",
        type=["png","jpg","jpeg","pdf","py","txt","js","cpp"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file

    st.markdown("---")

    st.markdown(f"👤 **{st.session_state.user}**")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.messages = []
        st.session_state.uploaded_file = None
        st.rerun()

# ==============================
# CHAT UI
# ==============================
st.title("CodeStore AI Assistant")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask coding questions...")

if prompt:
    if st.session_state.chat_id is None:
        st.session_state.chat_id = create_chat(st.session_state.user, prompt[:30])

    display = prompt

    if st.session_state.uploaded_file:
        display = f"📎 {st.session_state.uploaded_file.name}\n\n{prompt}"

    st.session_state.messages.append({"role": "user", "content": display})

    if st.session_state.chat_id:
        save_message(st.session_state.chat_id, "user", display)

    with st.chat_message("user"):
        st.markdown(display)

    file_context = ""
    if st.session_state.uploaded_file:
        f = st.session_state.uploaded_file
        if f.name.endswith(".pdf"):
            file_context = extract_pdf_text(f)
        else:
            file_context = extract_code_text(f)

    response = ollama_chat(f"{prompt}\n\n{file_context}")

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    if st.session_state.chat_id:
        save_message(st.session_state.chat_id, "assistant", response)