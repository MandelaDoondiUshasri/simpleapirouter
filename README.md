# 🗨️ Simple API Router 

A Django-based chatbot that can **detect intents**, extract parameters, and return appropriate responses for three core functions:

- 🌤 **Get Weather** — Simulated weather forecast for a given city.
- 😂 **Get Joke** — Returns a random joke from a predefined list.
- ➕ **Add Numbers** — Calculates the sum of two numbers.

This project demonstrates **basic NLP routing** using keyword matching and regex, and is designed for both **CLI demo** and **API usage** — **without Postman**.

---

## 🚀 Features
- **Intent Detection** using keyword mapping.
- **Parameter Extraction**:
  - City names (for weather queries).
  - Numeric values (for addition queries).
- **Function Dispatching**:
  - `getWeather(city)`
  - `getJoke()`
  - `addNumbers(a, b)`
- Works via:
  - **Command Line Interface (CLI)**
  - **Django REST API endpoint** (`/chat/`)
- **Extensible** — easily add more intents & handlers.

---

## 📂 Project Structure
```

chatbot\_project/
├── chatbot\_project/       # Django project settings
├── chatbot\_app/           # App with intents, extractors, handlers, dispatcher
├── demo.py                # CLI demo script
├── requirements.txt       # Dependencies
├── README.md              # This file
└── MODEL\_DOC.md           # NLP approach & logic explanation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Suryareddy180/simpleapirouter.git
cd simpleapirouter
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* **Windows**: `venv\Scripts\activate`
* **Mac/Linux**: `source venv/bin/activate`

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

---

## ▶️ Usage

### 🔹 Run CLI Demo

```bash
python demo.py
```

Sample Output:

```json
{
  "query": "What’s the weather in Delhi?",
  "intent": "GET_WEATHER",
  "parameters": {"city": "Delhi"},
  "result": "Weather for Delhi: Sunny, 28°C (simulated)",
  "notes": ""
}
```

### 🔹 Run Django API

```bash
python manage.py runserver
```

Send POST request (using curl):

```bash
curl -X POST http://127.0.0.1:8000/chat/ \
     -H "Content-Type: application/json" \
     -d '{"query": "Tell me a joke"}'
```

Example Response:

```json
{
  "query": "Tell me a joke",
  "intent": "GET_JOKE",
  "parameters": {},
  "result": "Why don’t skeletons fight each other? They don’t have the guts.",
  "notes": ""
}
```

---

## 🛠 Technologies Used

* **Django** — Backend framework
* **Django REST Framework** — API creation
* **Regex** — Parameter extraction
* **Python** — Core language

---

## 📄 MODEL\_DOC.md

This document explains:

* NLP approach
* Regex patterns used
* Fallback logic for missing parameters
* Extensibility guidelines

---

## 📌 Future Enhancements

* Add live weather API integration.
* Add more joke sources (e.g., external APIs).
* Expand to more NLP-based intents.
* Add voice input support.

---

## 👨‍💻 Author

**Doondi Usha Sri**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/mdushasri/)

```

