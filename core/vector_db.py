from langchain_community.vectorstores import FAISS

def build_vector_db(texts: list[str], embedder):
    return FAISS.from_texts(texts, embedder)

def save_vector_db(db, path="vector_store"):
    db.save_local(path)

# def load_vector_db(path, embedder):
#     return FAISS.load_local(path, embedder)
def load_vector_db(path, embedder):
    return FAISS.load_local(
        path,
        embedder,
        allow_dangerous_deserialization=True
    )

