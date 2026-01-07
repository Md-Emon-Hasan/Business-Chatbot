from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from data.documents import load_documents

def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    docs = load_documents()
    vectorstore = Chroma.from_documents(docs, embedding=embeddings)

    return vectorstore.as_retriever(search_kwargs={"k": 3})
