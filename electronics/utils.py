# utils.py
import json

JSON_FILE = 'path/to/your/data.json'

def load_data():
    with open(JSON_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)
