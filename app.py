from flask import Flask, render_template, request, jsonify
from utils.rag_pipeline import process_pdfs, ask_question

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("files")

    filepaths = []

    for file in files:
        path = f"uploads/{file.filename}"
        file.save(path)
        filepaths.append(path)

    process_pdfs(filepaths)

    return jsonify({"message": "PDFs uploaded successfully"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data["message"]

    answer = ask_question(question)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
