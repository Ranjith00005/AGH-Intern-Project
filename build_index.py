import os
from loaders import load_file
from core.embedder import get_embedder
from core.vector_db import build_vector_db, save_vector_db

DATA_DIR = "data"

FILES = [
    "colleges.json",
    "sample.txt",
    "document.pdf",
    "college.js"
]

def main():
    all_docs = []

    for file in FILES:
        file_path = os.path.join(DATA_DIR, file)
        docs = load_file(file_path)
        all_docs.extend(docs)

    embedder = get_embedder()
    db = build_vector_db(all_docs, embedder)
    save_vector_db(db)

    print("✅ Vector DB built from multiple documents")

if __name__ == "__main__":
    main()
