import re

def extract_city(query):
    match = re.search(r"(?:in|at|for)\s+([A-Za-z][A-Za-z\s\-]{1,40})", query, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_numbers(query):
    numbers = re.findall(r"[-+]?\d*\.?\d+", query)
    return [float(n) for n in numbers[:2]] if numbers else []
