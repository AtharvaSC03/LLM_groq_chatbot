import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq-compatible client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# UI
st.set_page_config(page_title="Groq Coding Copilot")
st.title("🤖 Groq Coding Copilot")
st.markdown("Ask any coding-related question!")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful programming assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.markdown(f"**Copilot:** {answer}")
