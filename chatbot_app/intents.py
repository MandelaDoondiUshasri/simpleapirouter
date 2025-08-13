INTENT_KEYWORDS = {
    'GET_WEATHER': ['weather', 'temperature', 'forecast'],
    'GET_JOKE': ['joke', 'funny', 'laugh'],
    'ADD_NUMBERS': ['add', 'sum', 'plus']
}

def detect_intent(query):
    text = query.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(k in text for k in keywords):
            return intent
    return 'UNKNOWN'
