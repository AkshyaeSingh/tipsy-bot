# tools/log_order.py
import requests
import os

def log_order(query: str) -> str:
    url = os.environ["SUPABASE_URL"] + "/rest/v1/drink_orders"
    headers = {
        "apikey": os.environ["SUPABASE_KEY"],
        "Authorization": f"Bearer {os.environ['SUPABASE_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "customer_id": "user123",  # later from memory
        "drink": query,
    }
    requests.post(url, json=data, headers=headers)
    return "Order logged in database."