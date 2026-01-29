from dotenv import load_dotenv
load_dotenv()

from core.embedder import get_embedder
from core.vector_db import load_vector_db
from core.retriever import retrieve
from core.groq_llm import get_groq_client, generate_answer

def main():
    embedder = get_embedder()
    db = load_vector_db("vector_store", embedder)
    client = get_groq_client()

    print("🧠 RAG Chat Ready. Type 'exit' to quit.\n")

    while True: # error 1 for not true
        question = input("Ask: ")
        if question.lower() == "exit":
            break

        docs = retrieve(db, question)
        context = "\n".join([d.page_content for d in docs])

        answer = generate_answer(client, context, question)
        print("\nAnswer:\n", answer, "\n")

if __name__ == "__main__":
    main()
