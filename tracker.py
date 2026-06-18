import json, os
from datetime import datetime

FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_expenses(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_expense(amount, category, note):
    data = load_expenses()
    data.append({
        "amount": amount,
        "category": category.capitalize(),
        "note": note,
        "date": datetime.today().strftime("%Y-%m-%d")
    })
    save_expenses(data)