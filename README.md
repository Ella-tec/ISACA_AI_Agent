# ISACA AI Chapter Support Agent

An intelligent chatbot assistant designed to support ISACA chapter members by answering questions using approved chapter content. Built with FastAPI, OpenAI, and a lightweight JSON vector store, it provides accurate, context-aware responses while logging all interactions for review.

---

## 📁 Project Structure

```
isaca-ai-agent/
├── app/
│   ├── admin/           # Admin utilities (content approval, ingestion)
│   ├── database/        # SQLite setup and interaction logging
│   ├── services/        # Core logic: embeddings, retrieval, OpenAI chat
│   ├── utils/           # Helpers: chunking, text formatting, etc.
│   └── main.py          # FastAPI app entry point
├── data/
│   ├── approved/        # Place approved source documents here
│   └── vector_store/    # JSON vector store (auto-generated on ingest)
├── logs/                # SQLite database for interaction logs
├── .env                 # Your private environment variables (never commit)
├── .env.example         # Safe template to share with teammates
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🧩 Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Backend API  | FastAPI                             |
| AI / LLM     | OpenAI API (GPT-4o + Embeddings)    |
| Vector Store | JSON file-based store               |
| Logging DB   | SQLite                              |
| Runtime      | Python 3.10+                        |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/isaca-ai-agent.git
cd isaca-ai-agent
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setting Up Your `.env` File

The `.env` file stores sensitive credentials and configuration that should **never** be committed to version control. Here's how to create, fill, and place it correctly.

### Where to Put It

Place the `.env` file in the **root of your project** (same level as `main.py` and `requirements.txt`):

```
isaca-ai-agent/
├── .env          ← right here
├── app/
├── data/
└── ...
```

### How to Create It

**Option A — From the terminal:**

```bash
# macOS / Linux
touch .env

# Windows (PowerShell)
New-Item .env -ItemType File
```

**Option B — Copy from the example template:**

```bash
cp .env.example .env
```

### How to Fill It

Open `.env` in any text editor and add the following key-value pairs:

```env
# --- OpenAI Configuration ---
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-small

# --- Storage Paths ---
VECTOR_STORE_PATH=data/vector_store/store.json
DB_PATH=logs/interactions.db

# --- App Settings ---
APP_ENV=development
MAX_TOKENS=1000
TOP_K_RESULTS=5
```

| Variable             | Description                                            | Where to Get It                          |
|----------------------|--------------------------------------------------------|------------------------------------------|
| `OPENAI_API_KEY`     | Your secret OpenAI API key                             | platform.openai.com → API Keys           |
| `OPENAI_MODEL`       | The GPT model to use for chat responses                | Use `gpt-4o` or `gpt-3.5-turbo`         |
| `EMBEDDING_MODEL`    | The model used to generate vector embeddings           | Use `text-embedding-3-small`             |
| `VECTOR_STORE_PATH`  | Path to the JSON file that stores embedded content     | Leave as default unless customized       |
| `DB_PATH`            | Path to the SQLite file for logging chat interactions  | Leave as default unless customized       |
| `APP_ENV`            | Runtime environment (`development` or `production`)    | Set manually                             |
| `MAX_TOKENS`         | Max tokens for each OpenAI response                    | Adjust based on cost/length preference   |
| `TOP_K_RESULTS`      | Number of vector chunks retrieved per query            | Default `5` works well                  |

### Protecting Your `.env`

Make sure `.env` is excluded from Git by confirming it is listed in `.gitignore`:

```bash
echo ".env" >> .gitignore
```

Share a **safe template** with teammates instead:

```bash
cp .env .env.example
# Then open .env.example and replace all real values with placeholders
```

---

## 🚀 Running the Backend

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

| URL                              | Description              |
|----------------------------------|--------------------------|
| `http://localhost:8000`          | Base API                 |
| `http://localhost:8000/docs`     | Swagger interactive docs |
| `http://localhost:8000/redoc`    | ReDoc API reference      |

---

## 📤 Uploading Approved Content

Only approved documents should be ingested into the vector store.

### Step 1 — Add Documents

Place approved `.pdf`, `.txt`, or `.docx` files into:

```
data/approved/
```

### Step 2 — Run the Ingestion Script

```bash
python -m app.admin.ingest
```

This will:
1. Read all files from `data/approved/`
2. Split text into chunks
3. Generate OpenAI embeddings for each chunk
4. Save everything to `data/vector_store/store.json`

### Step 3 — Verify the Vector Store

```bash
python -m app.admin.verify_store
```

Expected output:

```
✅ Vector store loaded: 142 chunks from 6 documents.
```

---

## 🧪 Testing the Chatbot

### Option A — Swagger UI (Browser)

1. Open `http://localhost:8000/docs`
2. Find the `POST /chat` endpoint
3. Click **Try it out**
4. Enter a test payload:

```json
{
  "message": "What are the benefits of ISACA membership?"
}
```

5. Click **Execute** and review the response.

### Option B — Terminal (curl)

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What certifications does ISACA offer?"}'
```

### Option C — Python Test Script

```bash
python -m app.utils.test_chat
```

---

## 📋 Viewing Interaction Logs

All conversations are logged to the SQLite database. To view them:

```bash
python -m app.database.view_logs
```

Or open the database directly with any SQLite viewer (e.g., DB Browser for SQLite):

```
logs/interactions.db
```

---

## 🛠 Troubleshooting

| Issue                              | Likely Cause                          | Fix                                              |
|------------------------------------|---------------------------------------|--------------------------------------------------|
| `OPENAI_API_KEY not found`         | `.env` not loaded or missing key      | Check `.env` file location and key name          |
| `Vector store is empty`            | Ingest script not run yet             | Run `python -m app.admin.ingest`                 |
| `No module named 'fastapi'`        | Virtual environment not activated     | Run `source venv/bin/activate`                   |
| `Port 8000 already in use`         | Another process using the port        | Use `--port 8001` or kill the existing process   |
| Responses are off-topic            | Low-quality or missing approved docs  | Review and re-ingest content in `data/approved/` |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is maintained by the ISACA AI Chapter. All approved content remains the property of its respective authors.
