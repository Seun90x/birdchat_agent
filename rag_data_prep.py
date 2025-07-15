
import sqlite3
import pandas as pd
from langchain.docstore.document import Document

def table_to_docs(db_path, table_name):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    
    docs = []
    for _, row in df.iterrows():
        summary = f"{table_name} entry for {row.get('Scientific_Name', 'unknown species')}:\n"
        details = "; ".join([f"{col}: {val}" for col, val in row.items() if pd.notnull(val)])
        doc_text = summary + details
        docs.append(Document(page_content=doc_text, metadata={"table": table_name}))
    return docs

def all_docs(db_path):
    docs = []
    for table in ["avonet", "avilist", "bird_leg_color"]:
        docs.extend(table_to_docs(db_path, table))
    return docs
