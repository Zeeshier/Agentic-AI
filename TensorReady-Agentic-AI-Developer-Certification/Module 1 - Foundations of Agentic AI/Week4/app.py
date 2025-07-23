import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 1. Load PDF and split into chunks
def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

# 2. Create vector store from documents
def create_vector_store(docs, index_path="vector_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)
    return vectorstore

# 3. Load existing vector store
def load_vector_store(index_path="vector_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings)

# 4. Define custom prompt
prompt = PromptTemplate(
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

# 5. Build the QA chain
def build_qa_chain(vectorstore):
    llm = ChatGroq(model_name="qwen-qwq-32b", temperature=0, api_key=api_key)
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

# 6. Main function
def main():
    pdf_path = "paper.pdf"
    user_question = "Summarize the main findings of the paper."

    if not os.path.exists("vector_index"):
        print("[INFO] No vector index found. Creating a new one...")
        documents = load_and_split_pdf(pdf_path)
        vectorstore = create_vector_store(documents)
    else:
        print("[INFO] Vector index found. Loading it...")
        vectorstore = load_vector_store()

    qa_chain = build_qa_chain(vectorstore)
    answer = qa_chain.run(user_question)

    print("\n💡 AI Response:\n", answer)

# Run the app
if __name__ == "__main__":
    main()
