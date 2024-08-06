from openai import OpenAI
import streamlit as st
from ml import rqa

st.title("ChatGPT-like clone")

client = OpenAI(api_key=API)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        result = rqa("PAKAI BAHASA INDONESIA, " + prompt)['result']
        full_response = ""
        for chunk in result.split():
            full_response += chunk + " "
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
