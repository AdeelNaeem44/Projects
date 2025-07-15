# 🧠 GenAI Tools Collection by Adeel Naeem

Welcome to my repository of AI-powered projects!  
This repo features intelligent agents built using **LangChain**, **Gemini 1.5**, **FastAPI**, **Streamlit**, and more — designed to handle tasks like currency conversion, web-assisted Q&A, and RAG-based answering.

---

## 📦 Projects Included

### 💱 ForexGenie – Currency Converter Agent
> A LangChain ReAct agent that uses Gemini + ExchangeRate-API to convert currencies via natural language queries.  
Example: _"Convert 100 USD to PKR"_

📁 `./ForexGenie/`  
🛠️ Deployed with: Streamlit or FastAPI

---

### 🌐 AskAnything – Web Search + QA Agent
> An agent that uses DuckDuckGo search + Gemini to answer current or general knowledge questions.  
Example: _"Who is the Prime Minister of Pakistan?"_

📁 `./AskAnything/`  
🛠️ Deployed with: FastAPI

---

### 🎥 RAG Chatbot – YouTube Video QA
> Uses YouTube transcripts + FAISS + Gemini for Retrieval-Augmented QA.  
Example: _"Summarize this video"_ or _"What did the speaker say about AI risks?"_

📁 `./RAG-Chatbot/`  
🛠️ Deployed with: Streamlit

---

## 🧱 Tech Stack

- [x] **LangChain** (ReAct agent, tools, chains)
- [x] **Google Gemini 1.5 API** via `langchain-google-genai`
- [x] **FastAPI** or **Streamlit** for deployment
- [x] **DuckDuckGo Search Tool**, **ExchangeRate-API**
- [x] **Python 3.10+**

---

## 🧪 Installation (General Steps)

```bash
# Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <project-folder>

# Install dependencies
pip install -r requirements.txt

# Run Streamlit or FastAPI app
# For Streamlit
streamlit run app.py

# For FastAPI
uvicorn main:app --reload
