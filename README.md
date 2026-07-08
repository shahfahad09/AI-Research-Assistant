# 🤖 AI Research Assistant

A Retrieval-Augmented Generation (RAG) based AI Research Assistant built with **FastAPI**, **Google Gemini API**, and **ChromaDB**. The application allows users to upload research PDFs, perform semantic search, and receive AI-generated answers with source citations.

---

## 📌 Features

- 📄 Upload PDF research documents
- 📝 Automatic text extraction
- ✂️ Intelligent text chunking
- 🔍 Semantic search using ChromaDB
- 🤖 AI-powered question answering with Google Gemini
- 📚 Retrieval-Augmented Generation (RAG)
- 📑 Source-aware responses with citations
- 🗄 Persistent vector database
- 🌐 Simple web interface using FastAPI

---

## 🏗️ Project Architecture

```
User
   │
   ▼
Upload PDF
   │
   ▼
Extract Text (PyMuPDF)
   │
   ▼
Text Chunking
   │
   ▼
Gemini Embeddings
   │
   ▼
ChromaDB
   │
   ▼
Semantic Retrieval
   │
   ▼
Gemini 2.5 Flash
   │
   ▼
Research Answer + Citations
```

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Backend | FastAPI |
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Gemini Embedding API |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| Text Chunking | LangChain Text Splitter |
| Frontend | HTML, CSS |
| Environment | Python Dotenv |

---

## 📂 Project Structure

```
AI-Research-Assistant/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── config.py
│   └── main.py
│
├── uploads/
├── chroma_db/
├── models/
├── screenshots/
├── demo_video/
│
├── .env
├── requirements.txt
├── README.md
└── test_gemini.py
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/shahfahad09/AI-Research-Assistant.git

cd AI-Research-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 💡 Workflow

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split text into semantic chunks.
4. Generate embeddings using Gemini.
5. Store embeddings in ChromaDB.
6. Ask research questions.
7. Retrieve relevant chunks.
8. Gemini generates an answer with citations.

---

<img width="1602" height="555" alt="image" src="https://github.com/user-attachments/assets/2a724447-e485-4a6e-b9fd-d0712cc55176" />


### Home Page

<img width="1638" height="1042" alt="image" src="https://github.com/user-attachments/assets/f0a0d9b6-36e0-4e0d-ba73-e9f75516f076" />


### PDF Upload

<img width="1642" height="975" alt="image" src="https://github.com/user-attachments/assets/51e1d149-82cf-4d2d-a737-f77b64aaf663" />
<img width="1607" height="1031" alt="image" src="https://github.com/user-attachments/assets/7cc7815c-2d9c-40f2-a752-b41af91ebe01" />


### AI Generated Answer

<img width="1628" height="1023" alt="image" src="https://github.com/user-attachments/assets/a7875469-301d-49ad-967d-2d0640bf7924" />
<img width="1295" height="823" alt="image" src="https://github.com/user-attachments/assets/ee4a508e-dcac-4c35-bdb9-f7e099bc5e40" />
<img width="1237" height="1021" alt="image" src="https://github.com/user-attachments/assets/70900588-c815-4e82-9b3a-142116c6bb27" />
<img width="1235" height="395" alt="image" src="https://github.com/user-attachments/assets/8f095b0d-1307-49c6-9a7d-4e4768e5584b" />
<img width="1697" height="1110" alt="image" src="https://github.com/user-attachments/assets/f2a6fcdb-2199-4f21-b5c7-0ccea085073a" />




---

## 🎯 Future Improvements

- Multi-PDF support
- Chat history
- PDF summarization
- Download research reports
- User authentication
- Advanced citation formatting
- Workflow automation using n8n
- Cloud deployment

---

## 📚 Applications

- Academic Research
- Literature Review
- Enterprise Knowledge Management
- Technical Documentation
- Research Automation
- AI-powered Document Analysis

---

## 👨‍💻 Author

**Md. Shahfahad Khan**

Machine Learning Engineer | AI/ML Developer

📧 Email: khannishu522@gmail.com

🔗 GitHub: https://github.com/shahfahad09

🌐 Portfolio: https://shahfahad09.github.io/-khan/

---

## ⭐ If you like this project

Please consider giving it a **Star ⭐** on GitHub.
