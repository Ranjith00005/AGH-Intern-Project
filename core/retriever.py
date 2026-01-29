def retrieve(db, query: str, k: int = 3):
    return db.similarity_search(query, k=k)
