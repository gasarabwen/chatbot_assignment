# ChromaDB + OpenRouter Chatbot

This is a Streamlit chatbot app that:
- Loads knowledge base from an Excel file
- Embeds content using OpenRouter
- Stores vectors in ChromaDB
- Answers questions based on similarity search
- Deployable on Streamlit Cloud

## Setup (with venv)

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenRouter API key
   ```

4. **Ingest your knowledge base:**
   ```bash
   python ingest.py
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

6. **Deactivate the venv when done:**
   ```bash
   deactivate
   ```
