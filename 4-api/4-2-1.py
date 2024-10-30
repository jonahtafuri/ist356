'''
For this challenge, use Azure entity recognition API to extract entities from the following text.

"The Dallas Cowboys are a far better team than the New York Giants this year. The Giants have not won a conference game yet."

Using the API output, print each extracted entity and its type.
'''
'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/keyphrasextraction' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 4b407d68cb3e5943ef06e805' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=Skyrim%20is%20an%20awesome%20game%2C%20but%20Bloodborne%20has%20to%20be%20one%20of%20my%20favorite%20games'
'''
import requests as rq
import streamlit as st
import pandas as pd
def extract_entities(text: str):
    url = "https://cent.ischool-iot.net/api/azure/keyphrasextraction"
    headers = {"X-API-KEY": "4b407d68cb3e5943ef06e805"}
    data = {"text": text}
    response = rq.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()
    
# text = "Skyrim is an awesome game, but Bloodborne has to be one of my favorite games. Playstation is a great console."
input = st.text_area("Give me your thoughts")
process = st.button("Extract entities")

if process:
    result = extract_entities(input)
    entities = result['results']['documents'][0]['keyPhrases']
    st.write(entities)
    df = pd.DataFrame(entities, columns=["Entity"])
    st.dataframe(df)