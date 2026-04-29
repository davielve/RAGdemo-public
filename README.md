# 🤖 Local RAG Demo Setup

Welcome to your local RAG (Retrieval-Augmented Generation) setup! This project provides a fully functional, private, and local AI solution, allowing you to chat with your own documents without sending any data to the cloud.

<img width="493" height="530" alt="1777139716035" src="https://github.com/user-attachments/assets/9eb4727e-02fc-438a-bb17-b559ef6db080" />

---

## 🚀 Overview

This setup integrates best-in-class open-source tools to create a powerful knowledge base:
- **Ollama**: Runs your LLMs and Embedding models locally.
- **ChromaDB**: A fast vector database for storing your documents' "memory".
- **n8n**: The workflow engine that connects everything (ingestion and chat interface).
- **PostgreSQL**: Robust database for n8n's internal operations and chat memory.

---

## 🛠️ Tech Stack

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-FF6D5B?style=for-the-badge&logo=n8n&logoColor=white)

---

## 🧠 AI Models

A RAG system requires two different types of models to function:

1.  **Chat Model (LLM):** This is the "brain" that generates answers.
    - *Example:* `llama3.1` (8B or larger) or `phi3`.
2.  **Embedding Model:** This is a specialized model used to turn text into mathematical vectors (embeddings) so the database can "understand" and search your documents. **You cannot run a RAG system without an embedding model.**
    - *Example:* `nomic-embed-text` (highly recommended for local use).

---

## 📦 Installation

Follow these steps to get your system up and running in minutes.

### Prerequisites
- Docker and Docker Compose installed.

### Step 1: Run the Installation Script
We've simplified the setup with a script that creates folders, starts containers, and pulls the recommended AI models:

```bash
chmod +x installations_vejledning.sh
./installations_vejledning.sh
```

*The script will pull:*
- `llama3.1`: For the chat interface.
- `nomic-embed-text`: For document embeddings.

### Step 2: Access the Services
Once finished, you can access the tools at:
- **n8n interface**: [http://localhost:5678](http://localhost:5678)
- **ChromaDB API**: [http://localhost:8000](http://localhost:8000)
- **Ollama API**: [http://localhost:11435](http://localhost:11435)

---

## 🔑 Setting Up Credentials in n8n

After importing the workflows, you need to configure the following credentials within n8n:

### 1. Ollama API
- **Type**: Ollama API
- **Base URL**: `http://ollama:11434` (Note: Use `ollama` as the hostname inside Docker)

### 2. ChromaDB API
- **Type**: ChromaDB Self-Hosted API
- **Host**: `http://chromadb`
- **Port**: `8000`

### 3. PostgreSQL (for Chat Memory)
- **Host**: `postgres`
- **Database**: `n8n`
- **User**: `n8n`
- **Password**: `n8n_password`
- **Port**: `5432`

---

## ⚙️ Workflow Setup

To start using your RAG system, import the two provided workflows into n8n:

1. **Ingestion Workflow** (`workflows/rag-ingestion-workflow.json`): 
   - Reads files from the `knowledge_base/` folder, splits them into chunks, and saves them to ChromaDB using the **Embedding Model**.
2. **Chat Workflow** (`workflows/rag-chat-workflow.json`):
   - The interactive interface where you chat with your documents using the **Chat Model**.

---

## 📂 Project Structure

- `knowledge_base/`: Drop your `.txt` or `.pdf` files here.
- `workflows/`: Contains n8n workflow JSON files.
- `check_chroma.py`: A utility script to verify if data is correctly indexed.
- `docker-compose.yml`: Infrastructure definition.

---

## 🔍 Verification
To verify that ChromaDB has indexed your documents:
```bash
python3 check_chroma.py
```

Enjoy your private, local AI setup! 🚀
