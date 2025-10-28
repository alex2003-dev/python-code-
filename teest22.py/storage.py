import json
import os

file_name = "expenses.json"

def load_expenses():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        print("Error reading file")
        return []

def save_expenses(data):
    try:
        with open(file_name, "w") as f:
            json.dump(data, f, indent=2)
    except:
        print("Error saving file")
