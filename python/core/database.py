import json
import os

def read_products():
    """
    Loads product data from the JSON file and returns it as a list of dictionaries.
    """
    json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("⚠️ products.json not found.")
        return []
    except json.JSONDecodeError:
        print("⚠️ products.json is not a valid JSON.")
        return []
