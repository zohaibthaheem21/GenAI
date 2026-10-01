# RAG Book Assistant

A simple RAG application that allows users to upload a PDF book and ask questions based on its content.

## What it does

* Upload a PDF book
* Split the document into smaller chunks
* Create embeddings using Mistral AI
* Store documents in ChromaDB
* Retrieve relevant information using MMR
* Generate answers using Mistral AI

## Technologies

* Python
* Streamlit
* LangChain
* Mistral AI
* ChromaDB

## Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

Upload a PDF, create the vector database, and start asking questions.
