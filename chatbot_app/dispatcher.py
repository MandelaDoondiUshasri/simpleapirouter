from .intents import detect_intent
from .extractors import extract_city, extract_numbers
from .handlers import getWeather, getJoke, addNumbers

def process_query(query):
    intent = detect_intent(query)
    params, result, notes = {}, "", ""

    if intent == 'GET_WEATHER':
        city = extract_city(query)
        params['city'] = city
        result = getWeather(city)
        if not city:
            notes = "City not detected."

    elif intent == 'GET_JOKE':
        result = getJoke()

    elif intent == 'ADD_NUMBERS':
        nums = extract_numbers(query)
        if len(nums) == 2:
            params['num1'], params['num2'] = nums
            result = addNumbers(nums[0], nums[1])
        else:
            notes = "Need two numbers."

    else:
        result = "Unknown request. Try asking about weather, a joke, or addition."

    return {
        "query": query,
        "intent": intent,
        "parameters": params,
        "result": result,
        "notes": notes
    }
