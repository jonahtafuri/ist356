from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/hello")    # Define a route
def root():      # Define a function that will be called when the route is requested
    return {"message": "Hello World"} # Serializes to JSON automatically

@app.get("/hi/{name}")
def hi(name: str):
    return {"message": f"Hi {name}"}



@app.get("/roll/{number}d{sides}")
def roll_dice(number: int, sides: int):
    import random

    rolls = 0
    for i in range(number):
        rolls += random.randint(1, sides)

    return {"sum": rolls,
            "sides" : sides,
            "dice_rolled": number
            }