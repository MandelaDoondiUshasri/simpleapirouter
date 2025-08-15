
# NLP Routing & Logic Documentation

## 📌 Project Overview
This project is a **simple intent-based API router** built using Django and Django REST Framework.  
It demonstrates **Natural Language Processing (NLP) routing** via **keyword-based intent detection** and **regex parameter extraction**.

---

## 🎯 Core Functionalities
1. **Get Weather** — Returns simulated weather for a city.
2. **Get Joke** — Returns a random joke from a list.
3. **Add Numbers** — Adds two numbers and returns the result.

---

## ⚙️ NLP Approach

### 1️⃣ **Intent Detection**
We use **keyword mapping** for each intent:

| Intent        | Keywords                       |
|---------------|--------------------------------|
| GET_WEATHER   | `weather`, `temperature`, `forecast` |
| GET_JOKE      | `joke`, `funny`, `laugh`       |
| ADD_NUMBERS   | `add`, `sum`, `plus`           |

**Process:**
1. Convert query to lowercase.
2. Remove punctuation (if needed).
3. Match keywords against the query.
4. Return the first matched intent or `UNKNOWN`.

---

### 2️⃣ **Parameter Extraction**
#### 📍 **City Extraction**
- Regex:  
```regex
(?:in|at|for)\s+([A-Za-z][A-Za-z\s\-]{1,40})
````

* Captures the city name following `in`, `at`, or `for`.
* Example:
  Query → `"What’s the weather in Delhi?"`
  Extracted → `"Delhi"`

#### 🔢 **Number Extraction**

* Regex:

```regex
[-+]?\d*\.?\d+
```

* Captures integers, decimals, and signed numbers.
* Only the **first two** numbers are used.
* Example:
  Query → `"Add 3.5 and -2"`
  Extracted → `[3.5, -2.0]`

---

### 3️⃣ **Dispatcher**

The **dispatcher** maps the detected intent to a handler:

```python
DISPATCHER = {
    'GET_WEATHER': getWeather,
    'GET_JOKE': getJoke,
    'ADD_NUMBERS': addNumbers
}
```

* If `UNKNOWN`, returns a helpful fallback message.
* Passes extracted parameters to the correct handler.

---

### 4️⃣ **Handlers**

#### `getWeather(city)`

* Simulates a weather forecast.
* Example output:
  `"Weather for Delhi: Sunny, 28°C (simulated)"`

#### `getJoke()`

* Returns a random joke from a predefined list.

#### `addNumbers(a, b)`

* Returns formatted sum.
* Example: `"3.5 + -2.0 = 1.5"`

---

## 🛠 Error Handling

* **Unknown Intent** → `"Unknown request. Try asking about weather, a joke, or addition."`
* **Missing Parameters**:

  * Weather: `"City not detected."`
  * Add: `"Need two numbers."`
* **Multiple Matches** → First match is used; ambiguity noted in `notes` field.

---

## 📊 Example Outputs

**Input:**

```
"What’s the weather in Delhi?"
```

**Output:**

```json
{
  "query": "What’s the weather in Delhi?",
  "intent": "GET_WEATHER",
  "parameters": {"city": "Delhi"},
  "result": "Weather for Delhi: Sunny, 28°C (simulated)",
  "notes": ""
}
```

**Input:**

```
"Add 12 and 8"
```

**Output:**

```json
{
  "query": "Add 12 and 8",
  "intent": "ADD_NUMBERS",
  "parameters": {"num1": 12.0, "num2": 8.0},
  "result": "12.0 + 8.0 = 20.0",
  "notes": ""
}
```

---

## 🔮 Future Enhancements

* Integrate **real weather API** (e.g., OpenWeatherMap).
* Use **spaCy** or **NLTK** for more accurate intent detection & entity extraction.
* Add **more intents** (e.g., news, currency conversion, time).
* Improve **error handling** for complex queries.

---

## 👨‍💻 Author

**Doondi Usha Sri**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/mdushasri/)

```

Do you want me to now give you the **exact git commands** so you can commit & push these new docs to your `simpleapirouter` repo? That way everything is live in 2 minutes.
```
