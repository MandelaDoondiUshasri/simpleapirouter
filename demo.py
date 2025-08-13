import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')
django.setup()

from chatbot_app.dispatcher import process_query

queries = [
    "What’s the weather in Delhi?",
    "Tell me a joke",
    "Add 12 and 8",
    "sum 3.5 and 2.1",
    "weather forecast for Mumbai",
    "joke please",
    "add numbers"
]

for q in queries:
    print(process_query(q))
    print("-" * 50)
