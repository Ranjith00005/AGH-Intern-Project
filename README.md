🧠 Universal RAG System using Groq API

A Retrieval-Augmented Generation (RAG) system that allows users to ask natural language questions over their own documents (JSON, TXT, PDF).
The system retrieves relevant information using semantic search and generates accurate, grounded answers using Groq-hosted LLaMA models.

🚀 Features

🔍 Semantic search using vector embeddings

📄 Supports JSON, TXT, and PDF documents

⚡ Ultra-fast LLM inference via Groq API

🧠 Uses Retrieval-Augmented Generation (RAG) to reduce hallucinations

🗂️ Modular, production-style project structure

🔐 Secure API key handling using .env

🏗️ Architecture Overview
User Query
    ↓
Query Embedding
    ↓
FAISS Vector Search
    ↓
Top-K Relevant Chunks
    ↓
Groq LLM (LLaMA 3.1)
    ↓
Final Answer

🛠️ Tech Stack
Component	Technology	Why Used
Language	Python	Strong AI ecosystem
Embeddings	Sentence Transformers	Semantic understanding
Vector DB	FAISS	Fast similarity search
LLM Inference	Groq API	Low-latency, scalable
Models	LLaMA 3.1	High-quality reasoning
Config	python-dotenv	Secure env handling
📁 Project Structure
doc_RAG/
│
├── core/
│   ├── embedder.py        # Embedding model
│   ├── vector_db.py       # FAISS operations
│   ├── retriever.py       # Similarity search
│   └── groq_llm.py        # Groq LLM integration
│
├── loaders/
│   ├── __init__.py        # Universal loader
│   ├── json_loader.py
│   ├── text_loader.py
│   └── pdf_loader.py
│
├── data/
│   ├── colleges.json
│   ├── college_from_js.json
│   ├── sample.txt
│   └── document.pdf
│
├── build_index.py         # Build vector database
├── rag_chat.py            # CLI chat interface
├── requirements.txt
├── .env
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/universal-rag-groq.git
cd universal-rag-groq

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here


⚠️ Do not commit .env to GitHub

4️⃣ Build the Vector Database
python build_index.py


Expected output:

✅ Vector DB built from multiple documents

5️⃣ Start the RAG Chat
python rag_chat.py

💬 Example Usage

Query:

get me the location of Ariyalur Engineering College


Response:

NH-227, Trichy-Chithambaram NH,
Karuppur-Senapathy Post,
Ariyalur District, Tamil Nadu

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
