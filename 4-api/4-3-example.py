import requests as rq
import streamlit as st
import pandas as pd

st.title("Amnesiac Skyrim Historian AI")
st.session_state['history'] = []
def respond_to_query(prompt: str):
    url = "https://cent.ischool-iot.net/api/openai/generate"
    headers = {"X-API-KEY": "4b407d68cb3e5943ef06e805"}
    data = {"query": prompt}
    response = rq.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()
    
input = st.text_area("Hello! what can I help you with?")
#append input to history

#flatten history

process = st.button("Use knowledge to answer")
process_2 = st.button("Don't use knowledge to answer")
if process:
    with st.spinner("thinking..."):
        st.write(respond_to_query(f"For the following question or statement give me how my statement is relevant to the Bethesda games Skyrim, Morrowind, or Oblivion. {input}"))

if process_2:
    with st.spinner("thinking..."):
        st.write(respond_to_query(input))
    