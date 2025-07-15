from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.document_loaders import CSVLoader
import os

def create_faiss_index(embedding=None):
    if embedding is None:
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    index_dir = "faiss_index"
    if os.path.exists(index_dir):
        print(f"🗑️ Removing old index at {index_dir}")
        import shutil
        shutil.rmtree(index_dir)

    all_docs = []
    for fname in ["data/avonet.csv", "data/avilist.csv", "data/bird_leg_color.csv"]:
        print(f"📄 Loading {fname}")
        loader = CSVLoader(file_path=fname)
        all_docs.extend(loader.load())

    print(f"✅ {len(all_docs)} documents prepared. Creating FAISS index...")
    db = FAISS.from_documents(all_docs, embedding)
    db.save_local(index_dir)
    print(f"✅ FAISS index saved to {index_dir}")
    return db

if __name__ == "__main__":
    create_faiss_index()
