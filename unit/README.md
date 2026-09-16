# ISACA AI Chapter Support Agent

A safe, local FastAPI application that helps ISACA chapter leaders find approved information using Retrieval‑Augmented Generation (RAG) and OpenAI.  
Everything runs only on your computer — no website hosting, no public exposure, no danger.

---

## 🚀 Tech Stack (Language Icons)

### Programming Languages
- 🐍 Python  
- ☕ Java  
- 🌐 HTML  
- 🎨 CSS  
- ⚙️ JSON  
- 🗄️ SQL (SQLite)

### Frameworks & Tools
- ⚡ FastAPI  
- 🔧 Uvicorn  
- 🤖 OpenAI API  
- 📦 SQLite  
- 📚 Markdown (README)

---

## 📌 Features
- 🔍 Searches approved ISACA content  
- 🤖 AI answers ONLY from your vector store  
- 🛡️ Safe, local backend (FastAPI)  
- 📚 Easy to add new documents  
- 📝 Automatic logging of all questions  
- 🚀 `/docs` interface for testing  
- 💾 SQLite logging (`logs.db`)  
- 📦 JSON knowledge base (`vector_store.json`)

---

## 📁 Project Structure
isaca_ai_agent.py        # Main single-file backend  
data/  
  vector_store.json      # Knowledge base  
  logs.db                # Chat history logs  
README.md                # This file  
logo.png                 # Optional logo  

---

## 🏢 Company Logo (Optional)
Place your logo file in the project root:
logo.png

To display it:
![Company Logo](./logo.png)

---

## ⚙️ Installation
1. Install dependencies:
   pip install fastapi uvicorn openai

2. Add your OpenAI API key (Windows):
   setx OPENAI_API_KEY "your_api_key_here"

3. Run the server:
   uvicorn isaca_ai_agent:app --reload

4. Open the API preview:
   http://127.0.0.1:8000/docs

---

## 📚 Adding Approved ISACA Content
Your AI reads from:
data/vector_store.json

Example content:
[
  {
    "title": "ISACA Chapter Basics",
    "text": "ISACA chapters are volunteer-led groups supported by the Chapter Experience team. Chapters provide local networking, training, and professional development opportunities."
  },
  {
    "title": "ISACA Membership Overview",
    "text": "ISACA members receive access to certifications, discounts on training, chapter events, and global professional communities."
  },
  {
    "title": "ISACA Certifications",
    "text": "ISACA offers globally recognized certifications including CISA, CISM, CRISC, and CGEIT."
  }
]

---

## 💬 Testing the Chatbot
In /docs, open POST /chat and enter:
{
  "user_id": "eliyas",
  "role": "chapter_leader",
  "question": "What is an ISACA chapter?"
}

---

## 📈 Viewing Logs
Your chatbot writes logs into:
data/logs.db

### Option A — VS Code
Install “SQLite Viewer”, right‑click logs.db → Open Database → click table logs.

### Option B — Python viewer
Create view_logs.py:
import sqlite3
conn = sqlite3.connect("data/logs.db")
cur = conn.cursor()
cur.execute("SELECT * FROM logs")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()

Run:
python view_logs.py

---

## 🔒 Safety
- Runs only on your computer  
- No public hosting  
- No website  
- No external danger  
- Only uses OpenAI API  

---

## 📜 License
Educational and chapter‑support use only.
