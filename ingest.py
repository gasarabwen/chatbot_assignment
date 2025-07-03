import chromadb
import pandas as pd

def ingest_excel_to_chroma(file_path="data/Chatbot Questions & Answers (2).xlsx"):
    df = pd.read_excel(file_path)
    
    # Convert columns to string and combine Questions and Answers columns for context
    df['Content'] = df['Questions'].astype(str).fillna('') + ' ' + df['Answers'].astype(str).fillna('')
    contents = df['Content'].dropna().tolist()

    # Use ChromaDB with default settings (no custom embedding function to avoid downloads)
    client = chromadb.Client()
    collection = client.get_or_create_collection("knowledge")

    for idx, content in enumerate(contents):
        collection.add(
            documents=[content],
            ids=[f"doc-{idx}"]
        )

    print("Ingested to ChromaDB.")

if __name__ == "__main__":
    ingest_excel_to_chroma()
