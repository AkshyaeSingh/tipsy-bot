# tools/make_drink.py
import requests

def make_drink(query: str) -> str:
    url = "https://exodust.app.n8n.cloud/webhook-test/25295c72-5a24-4638-8eab-5bb3adaf9a30"
    payload = {"drink": query}
    response = requests.post(url, json=payload)
    return f"Drink '{query}' has been sent to the bar for preparation!"