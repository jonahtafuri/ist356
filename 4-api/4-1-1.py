'''
## Challege 4-1-1

Write a streamlit to read from the url:

https://jsonplaceholder.typicode.com/users/

Then display the data in a pandas dataframe. 

 - use the requests library to get the data
 - use `json_normalize()` to convert the nested json data into a dataframe
'''
import requests as req
import pandas as pd
import streamlit as st

url = "https://jsonplaceholder.typicode.com/users/"
resp = req.get(url)
resp.raise_for_status()
data = resp.json()
df = pd.json_normalize(data)
st.dataframe(df)
