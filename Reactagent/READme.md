# 🤖 GemReAct

**GemReAct** is an intelligent AI agent powered by Google’s Gemini 1.5 Flash model and LangChain’s ReAct framework. It can perform reasoning and retrieve real-time information using external tools like DuckDuckGo Search.

---

## ✨ Features

- 🧠 **LLM-powered**: Uses Gemini 1.5 Flash via LangChain.
- 🔁 **ReAct Agent**: Implements Reasoning + Acting framework for better step-by-step thinking.
- 🔎 **Tool Integration**: Leverages DuckDuckGo search to answer up-to-date queries.
- 🔧 **Modular Design**: Easily extend with additional tools or LLMs.
- 📦 **Lightweight & Fast**: Focused only on the agent logic.

---

## 🧰 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Gemini 1.5 Flash (via `langchain-google-genai`)](https://ai.google.dev/)
- [DuckDuckGo Search Tool](https://pypi.org/project/duckduckgo-search/)
- Python 3.10+

---

## 🚀 How It Works

1. Loads a custom ReAct prompt from LangChain Hub.
2. Uses the Gemini LLM to interpret and reason about the input query.
3. If necessary, invokes the DuckDuckGo tool to fetch up-to-date information.
4. Returns a clear, contextual response to the user.

---

## 📁 File Structure

📦 GemReAct/
├── Agent.py # Main ReAct agent logic
├── requirements.txt # Required dependencies
├── README.md # Project documentation
