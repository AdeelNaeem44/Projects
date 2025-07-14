import streamlit as st
import time
from chatbot_agent import agent  # Ensure agent.run(query) returns a string

# Page config
st.set_page_config(page_title="💱 ForexGenie", layout="centered")

# Remove Streamlit's default padding
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
.chat-wrapper {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    max-width: 800px;
    margin: 0 auto 4rem auto;
    padding-top: 0.5rem;
}
.bubble-container {
    display: flex;
    width: 100%;
}
.bubble-container.user {
    justify-content: flex-end;
}
.bubble-container.assistant {
    justify-content: flex-start;
}
.chat-bubble {
    padding: 0.8rem 1.2rem;
    border-radius: 1rem;
    font-size: 16px;
    line-height: 1.5;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    width: fit-content;
    max-width: 80%;
    word-wrap: break-word;
}
.user-bubble {
    background-color: #1f6feb;
    color: white;
    text-align: right;
}
.assistant-bubble {
    background-color: #2c2c2c;
    color: white;
    border-left: 5px solid #00C9A7;
    text-align: left;
}
body {
    background-color: #0f1117;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("💱 ForexGenie")
st.markdown("_Smart + magical assistant — feel free to ask anything!_")

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input
query = st.chat_input("Ask me anything...")

# Add new user message (before rendering)
if query and query.strip():
    st.session_state.messages.append({"role": "user", "content": query})

    try:
        bot_reply = agent.run(query)
    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Render full conversation in ONE wrapper
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    role = msg["role"]
    container = "user" if role == "user" else "assistant"
    bubble = "user-bubble" if role == "user" else "assistant-bubble"
    st.markdown(f'''
        <div class="bubble-container {container}">
            <div class="chat-bubble {bubble}">{msg["content"]}</div>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
