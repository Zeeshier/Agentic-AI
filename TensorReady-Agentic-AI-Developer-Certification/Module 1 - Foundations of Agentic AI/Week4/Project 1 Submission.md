 # RAG-based AI assistant for scientific paper summarization and suggestion
## Project Overview
This project builds a smart PDF question-answering system using:

- LangChain for chaining components
- FAISS for vector-based document retrieval
- SentenceTransformers for document embedding
- ChatGroq (Qwen-QWQ-32B) as the LLM
- LangChain PromptTemplate for custom response formatting

The system allows users to ask questions about the content of a scientific paper (PDF), and get concise, accurate, and technical answers based on the document.

## Project Structure

```bash
scientific_paper_summarization_and_suggestion
├── data/paper.pdf          # Your input scientific paper
├── vector_index/           # FAISS index folder (auto-generated)
├── .env                    # Your API key
└── main.py                 # Main project script
└── notebook/notebook       # Project notebook 

```

## Step-by-Step Code Explanation
### 1. Environment Setup
```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```

Loads your GROQ API key from a .env file.

Always keep your keys secret and never hardcode them.

### 2. PDF Loading and Chunking
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)
```


Loads the PDF file using PyPDFLoader.

Splits the PDF into smaller chunks using RecursiveCharacterTextSplitter to make them fit LLM context windows.

### 3. Embedding and Creating a FAISS Vector Index
```python
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(docs, index_path="vector_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)
    return vectorstore
```


Converts text chunks into vectors using a HuggingFace model.
Saves vectors using FAISS to enable fast similarity search.

### 4.  Load an Existing Vector Store
```python
def load_vector_store(index_path="vector_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings)
```


Reloads a previously created FAISS vector index from disk.

### 5. Custom Prompt Template
```python
from langchain.prompts import PromptTemplate

CUSTOM_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a scientific research assistant.
Given the following context from scientific papers, answer the user's question.
Be concise, technical, and include any relevant research suggestions.

Context:
{context}

Question:
{question}

Answer:
"""
)
```

Defines how the LLM should respond.

It provides role-based instructions and formats the prompt cleanly.

### 6. Create Retrieval-Based QA Chain
```python
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

def create_qa_chain(vectorstore):
    llm = ChatGroq(model_name="qwen-qwq-32b", temperature=0, api_key=api_key)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": CUSTOM_PROMPT}
    )
    return qa_chain
```

Initializes the Qwen-32B model from Groq.

Uses RetrievalQA to combine vector-based context retrieval with the LLM.

chain_type="stuff" puts all retrieved documents directly into the prompt.

### 7. Main Function: Build or Load Vector Store & Run Query
```python
if __name__ == "__main__":
    pdf_path = "paper.pdf"
    user_query = "Summarize the main findings of the paper."

    if not os.path.exists("vector_index"):
        print("[INFO] No existing vector index found. Creating new one...")
        docs = load_and_split_pdf(pdf_path)
        vectorstore = create_vector_store(docs)
    else:
        print("[INFO] Loading existing vector index...")
        vectorstore = load_vector_store()

    qa_chain = create_qa_chain(vectorstore)
    response = qa_chain.run(user_query)
    print("\n💡 AI Response:\n", response)
```

### Workflow:
Check if a vector index already exists.

If not, load the PDF → chunk → embed → save FAISS index.

Create a QA chain with retrieval + Groq LLM.

Ask the user query and print the response.

###  .env File
Create a .env file in your project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### Requirements (install with pip)
```bash
pip install langchain langchain-community langchain-groq faiss-cpu sentence-transformers python-dotenv
```




