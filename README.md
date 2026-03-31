# 🚀 CodeStore AI Assistant

An intelligent, scalable AI-powered chatbot built using **Streamlit**, **PostgreSQL**, and **Ollama**, designed with a clean modular backend architecture.

---

## 🔥 Features

* 🔐 User Authentication (Signup / Login)
* 💬 Multi-Chat System with Session Handling
* 🧠 AI-Powered Responses (Ollama - LLaMA & DeepSeek)
* 📂 File Upload Support (PDF, Code Files)
* 🗄️ PostgreSQL Database Integration
* 📊 Persistent Chat History
* 🧩 Modular Backend Architecture (Production-ready structure)

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python (Modular Architecture)
* **Database:** PostgreSQL
* **AI Models:** Ollama (LLaMA 3.1, DeepSeek Coder)
* **Libraries:** psycopg2, PyPDF2

---

## 📂 Project Structure

```
CodeStoreAI-II/
│
├── frontend/
│   └── app.py                # Streamlit UI
│
├── backend/
│   └── app/
│       ├── api/
│       │   └── routes/
│       │       └── auth.py   # Authentication logic
│       │
│       ├── services/
│       │   ├── ai_engine.py      # AI interaction (Ollama)
│       │   ├── chat_manager.py   # Chat logic
│       │   └── file_handler.py   # File processing
│       │
│       ├── db/
│       │   └── db.py         # Database connection
│       │
│       ├── models/           # (Reserved for ORM models)
│       └── core/             # (Config & security - future use)
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/CodeStoreAI-II.git
cd CodeStoreAI-II
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup PostgreSQL

* Create database: `codestore_ai`
* Update credentials in:

```
backend/app/db/db.py
```

---

### 5️⃣ Run Ollama (Required)

Make sure Ollama is running locally:

```
ollama run llama3.1
```

---

### 6️⃣ Run Application

```
streamlit run frontend/app.py
```

---

## 🚀 Future Improvements

* 🔐 Google / Microsoft SSO Login
* ⚡ FastAPI Backend Integration
* ☁️ Cloud Deployment (AWS / GCP / Azure)
* 🧠 Chat Title Generation using AI
* 📊 Analytics Dashboard

---

## 👨‍💻 Author

**Umar Imam**

---

## ⭐ Notes

This project follows a **scalable backend architecture**, making it easy to extend into a full production-grade AI application.
