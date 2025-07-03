import streamlit as st
from chatbot import ask_chatbot

st.set_page_config(page_title="🧠 ChromaDB Chatbot")

st.title("📘 Chatbot with ChromaDB & OpenRouter")
query = st.text_input("Ask a question:")

if query:
    with st.spinner("Searching..."):
        response = ask_chatbot(query)
    st.success(response)
