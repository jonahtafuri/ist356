
import requests as req
import streamlit as st
from time import sleep

api_key = "4b407d68cb3e5943ef06e805"

st.title("Weather app")

def query_api(urt: str, params: dict):
    header = {"X-API-KEY": api_key}
    resp = req.get(f"https://cent.ischool-iot.net{urt}", params=params, headers=header)
    resp.raise_for_status()
    return resp.json()

address = st.text_input("Enter an address")
if address:
    with st.spinner("Getting weather..."):
        sleep(2)
        response = query_api("/api/google/geocode", {"location": address})
        # st.write(response)
        lat = response["results"][0]["geometry"]["location"]["lat"]
        lon = response["results"][0]["geometry"]["location"]["lng"]
        # st.write(f"lat: {lat}, lon: {lon}")
        response = query_api("/api/weather/current", {"units": "imperial", "lon": lon, "lat": lat})
        st.dataframe(response)
        temp = response['current']['temperature_2m']
        st.metric("Temperature", f"{temp}°F")



# response = query_api("api/weather/current", {"units": "imperial", "lon": -78.8, "lat": 43.0})
# st.write(response)