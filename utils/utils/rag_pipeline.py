from transformers import pipeline

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from utils.pdf_utils import load_pdfs

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

llm = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200
)

db = None

def process_pdfs(paths):
    global db

    chunks = load_pdfs(paths)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./db"
    )

def ask_question(question):
    docs = db.similarity_search(question, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm(prompt)

    return response[0]["generated_text"]
