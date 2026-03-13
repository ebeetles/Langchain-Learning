from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
collection_name = "computational_biology_papers"

if not os.path.exists(db_location):
    print("Vector database not found. Creating and indexing mpicker.pdf...")
    
    loader = PyPDFLoader("mpicker.pdf")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    documents = text_splitter.split_documents(data)

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=db_location
    )
else:
    vector_store = Chroma(
        collection_name=collection_name,
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
