# 🚀 FastAPI Backend for AI-Powered Video Q&A App

This is the **backend** for a full-stack web application built with **FastAPI**. It supports:

- ✅ **User authentication** (register, login)
- 🎥 **YouTube video loading and transcript extraction**
- 🧠 **Embeddings generation** using OpenAI
- 📦 **Vector storage** with Pinecone
- 🔍 **Semantic search**
- 🤖 **LLM responses** using OpenAI’s GPT models
- PostgreSQL for login and registeration

---

## 📁 Folder Structure

├── app/
│ ├── auth/ # Login and registration logic
│ ├── youtube/ # Video handling and transcript extraction
│ ├── vector/ # Pinecone vector DB logic
│ ├── llm/ # Query handling via OpenAI
│ └── schemas/ # Pydantic models
├── main.py # FastAPI entry point
├── requirements.txt
└── .env # Environment variables



---
