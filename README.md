# RAG-Bot
# RAG Chatbot for PDF Question Answering

A full-stack AI-powered chatbot that answers questions from uploaded PDF documents using Retrieval-Augmented Generation (RAG).

## Features

- Upload one or multiple PDFs
- Ask questions from documents
- Semantic search using embeddings
- Conversational chat interface
- PDF summarization
- Persistent vector database
- Source-aware responses

## Tech Stack

- Python
- Flask
- LangChain
- Hugging Face
- ChromaDB
- HTML/CSS/JavaScript

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
rag-pdf-chatbot/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── uploads/
├── db/
└── utils/
    ├── pdf_utils.py
    └── rag_pipeline.py
```
