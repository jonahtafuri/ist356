import requests as rq
import streamlit as st
import pandas as pd

st.title("Spell Checker AI")

def open_complete(prompt):
    url = "https://cent.ischool-iot.net/api/openai/generate"
    headers = {"X-API-KEY" : "4b407d68cb3e5943ef06e805"}
    data = {"query" : prompt}
    response = rq.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()

def spell_check(text):
    prompt = f"Please spell check the following text: \n{text}\n"
    prompt += "for each mispelled word, provide one suggested correction.\n return these as a list of dictionary in JSON format"
    response = open_complete(prompt)
    return response

input = st.text_area("Enter a sentence")
process = st.button("Check spelling")
if process:
    with st.spinner("Checking spelling..."):
        st.write(spell_check(input))