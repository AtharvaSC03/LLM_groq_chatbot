import streamlit as st
from openai import OpenAI

# UI Setup
st.set_page_config(page_title="Groq Coding Copilot")
st.title("🤖 Groq Coding Copilot")
st.markdown("Ask any coding-related question!")

# API Key Input
api_key = st.text_input("🔑 Enter your Groq API Key:", type="password")

# User message input
user_input = st.text_input("💬 You:", "")

# Proceed only if API key is provided
if api_key and user_input:
    try:
        with st.spinner("Thinking..."):
            # Initialize Groq-compatible client
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )

            # Get assistant response
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful programming assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            st.markdown(f"**🧠 Copilot:** {answer}")
    except Exception as e:
        st.error(f"Error: {e}")
