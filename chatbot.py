import chromadb
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://your-site.com",
    "X-Title": "Excel Chroma Chatbot"
}

CHAT_MODEL = "microsoft/wizardlm-2-8x22b"

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("knowledge")

def get_context(user_query, top_k=1):
    results = collection.query(
        query_texts=[user_query],
        n_results=top_k
    )
    return " ".join(results['documents'][0])

def ask_chatbot(user_input):
    context = get_context(user_input)

    res = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=HEADERS,
        json={
            "model": CHAT_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a helpful assistant. Use this context: {context}"},
                {"role": "user", "content": user_input}
            ]
        }
    )
    
    response_json = res.json()
    
    # Debug: print the actual response
    if 'choices' not in response_json:
        print("OpenRouter API error response:", response_json)
        if 'error' in response_json:
            return f"API Error: {response_json['error'].get('message', 'Unknown error')}"
        else:
            return f"Unexpected API response: {response_json}"
    
    return response_json['choices'][0]['message']['content']
