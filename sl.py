import streamlit as st
import time
from ml import rqa


st.title(f"TANYA :blue[GDPR] 🤖")
prompt = st.chat_input("Say something")
if prompt:
    st.subheader(f"Pertanyaan: ")
    st.code(prompt)
    st.subheader(f"Respon: ")
    message_placeholder = st.empty()
    
    with st.spinner('Loading...'):
        result = rqa("PAKAI BAHASA INDONESIA, " + prompt)['result']
    full_response = ""
  
    for chunk in result.split():
        full_response += chunk + " "
        time.sleep(0.05)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")

    message_placeholder.markdown(full_response)

