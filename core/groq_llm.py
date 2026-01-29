import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")  # ✅ ENV VARIABLE NAME
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")
    return Groq(api_key=api_key)

def generate_answer(client, context: str, question: str):
    prompt = f"""
You are a helpful assistant.
Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # fast & reliable on Groq
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
