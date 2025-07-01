# AskSphere — AI Chatbot Using Wikipedia + FLAN-T5

**AskSphere** is an intelligent, open-source chatbot that uses the Wikipedia API and Google’s FLAN-T5 Large model to answer questions naturally — without any paid APIs or backend services. It can handle both factual and educational queries and respond accordingly with either concise or elaborative answers.

## 🔍 Features

- Retrieves real-time content from Wikipedia
- Uses FLAN-T5 (via Hugging Face Transformers) to generate fluent, context-aware responses
- Automatically adapts the answer length based on the type of question:
  - Short factual or current topic → 1-line answer
  - Historical or educational topic → 2–3 sentence response
- Fully local and lightweight — no OpenAI, no billing, no backend
- Streamlit UI that mimics chat interaction

## 🧠 How It Works

1. User submits a question in the Streamlit interface.
2. The system searches Wikipedia for the most relevant article or summary.
3. If a summary isn't found, it builds a context block from full content.
4. A prompt is formed with the question and Wikipedia context.
5. The FLAN-T5 model generates an appropriate, natural-language response.
6. The answer is displayed in the chat area.

## 🛠️ Tech Stack

- Python
- [Wikipedia Python Package](https://pypi.org/project/wikipedia/)
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)
- FLAN-T5 Large Model (`google/flan-t5-large`)
- Streamlit (for UI)

## 📂 File Structure

asksphere/
├── app1.py # Streamlit chatbot app
├── chatbot_module.py # Wiki search + FLAN-T5 answer logic
├── test.py # Standalone CLI testing script
├── requirements.txt


## 🧪 Sample Questions

| Type       | Example                                         |
|------------|--------------------------------------------------|
| Factual    | Who is the current Prime Minister of Pakistan?   |
| Historical | What is the history of the Lahore Fort?          |
| Current    | Dollar rate in Pakistan today                    |
| Conceptual | What is Artificial Intelligence?                 |

## 💡 Challenges Faced

- Extracting relevant and readable context from long Wikipedia pages
- Handling ambiguous terms using search fallback
- Avoiding overly short or off-topic answers from the language model
- Managing Streamlit session state for smooth UI interaction

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/asksphere.git
cd asksphere

