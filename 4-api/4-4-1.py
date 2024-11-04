from fastapi import FastAPI, Query
import pandas as pd
import json
app = FastAPI()

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df = pd.read_csv(url)

@app.get("/api/flights/search")
def search_flights(type: str = Query(), code: str  = Query()):

    # departure_airport_code
    # arrival_airport_code
    if type == "dep":
        flights = df[df['departure_airport_code'] == code]
    elif type == "arr":
        flights = df[df['arrival_airport_code'] == code]
    else:
        return {"error": "Invalid type"}


    if type == 'dep':
        column = 'departure_airport_code'

    json_flights = flights.to_json(orient="records")
    return json.loads(json_flights)


