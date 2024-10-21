'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'
'''
import requests as req
import pandas as pd

if __name__ == "__main__":
    url = "https://cent.ischool-iot.net/api/funnyname/random"
    params = {"n": 3}
    resp = req.get(url, params=params)
    resp.raise_for_status()
    names = resp.text
    print(names)

    names = resp.json()

    for name in names:
        print(f"first: {name['first']}, last: {name['last']}")


def query_api(urt: str, params: dict):
    resp = req.get(f"https://cent.ischool-iot.net/{urt}", params=params)
    resp.raise_for_status()
    return resp.json()

response = query_api("api/funnyname/search", {"q": "joe"})
print(response)