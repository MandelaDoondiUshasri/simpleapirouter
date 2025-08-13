import random

def getWeather(city):
    return f"Weather for {city}: Sunny, 28°C (simulated)" if city else "City not provided."

def getJoke():
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why was the math book sad? It had too many problems."
    ]
    return random.choice(jokes)

def addNumbers(a, b):
    return f"{a} + {b} = {a + b}"
