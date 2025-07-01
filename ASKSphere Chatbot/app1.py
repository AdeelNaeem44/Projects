# app1.py

import streamlit as st
from chatbot_module1 import get_combined_answer

st.set_page_config(page_title="AskSphere Chatbot", page_icon="📚")

st.markdown("""
    <style>
        .stTextInput > div > div {
            margin: auto;
        }
        .chat-input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f0f2f6;
            padding: 10px 20px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            z-index: 100;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description at the top
st.title("AskSphere – Unique, global knowledge feel")
st.caption("Ask about education, history, or Recent News. Built with Wikipedia and FLAN-T5 model.")

# Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Show previous messages (scrollable)
with st.container():
    for msg in st.session_state.chat:
        if msg["role"] == "user":
            col1, col2 = st.columns([0.3, 0.7])
            with col2:
                st.markdown(f"""
                    <div style='text-align: right; background-color: #DCF8C6; padding: 10px 15px;
                    border-radius: 15px; margin-bottom: 5px;'>
                        <strong>You:</strong><br>{msg['text']}
                    </div>
                """, unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([0.7, 0.3])
            with col1:
                st.markdown(f"""
                    <div style='text-align: left; background-color: #F1F0F0; padding: 10px 15px;
                    border-radius: 15px; margin-bottom: 5px;'>
                        <strong>Bot:</strong><br>{msg['text']}
                    </div>
                """, unsafe_allow_html=True)

# Bottom fixed input field
with st.container():
    st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask your question:", label_visibility="collapsed", placeholder="Type your question here...")
        submitted = st.form_submit_button("Send")

        if submitted and user_input.strip():
            bot_response = get_combined_answer(user_input)

            st.session_state.chat.append({"role": "user", "text": user_input})
            st.session_state.chat.append({"role": "bot", "text": bot_response})
            st.rerun()
  # force re-render to scroll up
    st.markdown("</div>", unsafe_allow_html=True)
