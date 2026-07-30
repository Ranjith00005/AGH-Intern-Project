🧠 Universal Document RAG System using Groq API

A high-performance Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions over their own documents. The system retrieves the most relevant information using semantic vector search and generates context-aware, grounded responses using Groq-hosted Llama 3.1 models.

Designed with a modular architecture, this project supports multiple document formats and serves as a solid foundation for building AI-powered knowledge assistants, enterprise search systems, and document chatbots.

✨ Features
📄 Supports multiple document formats (PDF, TXT, JSON)
🔍 Semantic document retrieval using Sentence Transformers
⚡ Lightning-fast inference with Groq API
🧠 Retrieval-Augmented Generation (RAG) for accurate, context-aware responses
📚 Automatic document chunking and embedding generation
💾 High-speed similarity search using FAISS
🔐 Secure API key management with .env
🏗️ Modular and scalable project architecture
💻 Interactive command-line chat interface
🏛️ System Architecture
                ┌────────────┐
                │ User Query │
                └─────┬──────┘
                      │
                      ▼
          Generate Query Embedding
                      │
                      ▼
          FAISS Similarity Search
                      │
                      ▼
         Retrieve Top-K Relevant Chunks
                      │
                      ▼
       Prompt + Retrieved Context
                      │
                      ▼
             Groq Llama 3.1 API
                      │
                      ▼
        Context-Aware Final Response
🛠️ Tech Stack
Component	Technology	Purpose
Programming Language	Python	Core development
Embedding Model	Sentence Transformers	Semantic vector embeddings
Vector Database	FAISS	Efficient similarity search
Large Language Model	Llama 3.1	Response generation
LLM Inference	Groq API	Ultra-fast inference
Environment Management	python-dotenv	Secure API key storage
📂 Project Structure
doc_RAG/
│
├── core/
│   ├── embedder.py          # Generates embeddings
│   ├── vector_db.py         # FAISS index management
│   ├── retriever.py         # Semantic retrieval
│   └── groq_llm.py          # Groq LLM integration
│
├── loaders/
│   ├── __init__.py
│   ├── json_loader.py
│   ├── pdf_loader.py
│   └── text_loader.py
│
├── data/
│   ├── colleges.json
│   ├── college_from_js.json
│   ├── sample.txt
│   └── document.pdf
│
├── build_index.py           # Creates vector database
├── rag_chat.py              # Interactive chatbot
├── requirements.txt
├── .env
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/your-username/universal-document-rag.git

cd universal-document-rag
2. Install Dependencies
pip install -r requirements.txt
3. Configure Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_groq_api_key_here

Note: Never commit your .env file to version control.

4. Build the Vector Index
python build_index.py

Output

Loading documents...
Generating embeddings...
Building FAISS index...
Vector database created successfully.
5. Launch the Chat Interface
python rag_chat.py
💬 Example
Query
Where is Ariyalur Engineering College located?
Retrieved Context
NH-227, Trichy-Chidambaram Highway,
Karuppur-Senapathy Post,
Ariyalur District,
Tamil Nadu
Response
Ariyalur Engineering College is located on NH-227
(Trichy–Chidambaram Highway), Karuppur-Senapathy Post,
Ariyalur District, Tamil Nadu.
📈 Workflow
Load Documents
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
User Query
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Generate Response using Groq Llama
      │
      ▼
Final Answer
🎯 Applications
📚 Document Question Answering
🏢 Enterprise Knowledge Base
🎓 Educational Assistants
📑 Research Paper Search
📄 Legal & Policy Document Analysis
🏥 Healthcare Documentation
🤖 AI-powered Internal Chatbots
🚀 Future Enhancements
🌐 Web-based interface using Streamlit or FastAPI
🗄️ Support for additional vector databases (ChromaDB, Pinecone, Milvus)
📂 Drag-and-drop document uploads
💬 Conversation memory
🔄 Incremental document indexing
📊 Source citations and confidence scores
🖼️ OCR support for scanned PDFs
🌍 Multi-language document support
⭐ Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

📜 License

This project is licensed under the MIT License.

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and supports future improvements.
