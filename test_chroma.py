import chromadb

# Test connection to ChromaDB
try:
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("knowledge")
    
    # Test a simple query
    results = collection.query(
        query_texts=["admission"],
        n_results=1
    )
    
    print("ChromaDB test successful!")
    print(f"Found {len(results['documents'][0])} documents")
    if results['documents'][0]:
        print("Sample result:")
        print(results['documents'][0][0][:200] + "..." if len(results['documents'][0][0]) > 200 else results['documents'][0][0])
    
except Exception as e:
    print(f"ChromaDB test failed: {e}")
