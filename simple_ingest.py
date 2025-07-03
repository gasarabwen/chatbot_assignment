import chromadb
import pandas as pd

def simple_ingest():
    # Read the Excel file
    df = pd.read_excel("data/Chatbot Questions & Answers (2).xlsx")
    
    # Convert columns to string and combine Questions and Answers columns for context
    df['Content'] = df['Questions'].astype(str).fillna('') + ' ' + df['Answers'].astype(str).fillna('')
    contents = df['Content'].dropna().tolist()

    print(f"Found {len(contents)} entries to ingest")
    
    # Use ChromaDB with a very simple setup
    try:
        # Create a persistent client to avoid download issues
        client = chromadb.PersistentClient(path="./chroma_db")
        
        # Try to create collection without custom embedding function
        try:
            collection = client.delete_collection("knowledge")
            print("Deleted existing collection")
        except:
            pass
            
        collection = client.create_collection("knowledge")
        print("Created new collection")
        
        # Add documents in small batches to avoid timeouts
        batch_size = 5
        for i in range(0, len(contents), batch_size):
            batch = contents[i:i+batch_size]
            batch_ids = [f"doc-{j}" for j in range(i, i+len(batch))]
            
            print(f"Adding batch {i//batch_size + 1}/{(len(contents)-1)//batch_size + 1}")
            collection.add(
                documents=batch,
                ids=batch_ids
            )
        
        print(f"Successfully ingested {len(contents)} documents to ChromaDB!")
        
    except Exception as e:
        print(f"Error: {e}")
        print("ChromaDB is still trying to download the embedding model.")
        print("Please try again later when your internet connection is more stable.")

if __name__ == "__main__":
    simple_ingest()
