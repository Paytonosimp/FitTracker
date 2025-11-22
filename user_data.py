# user_data.py
# Handles user data storage

import json

user_data = {
    "workouts": [],
    "meals": []
}

def save_data(filepath='data.json'):
    with open(filepath, 'w') as f:
        json.dump(user_data, f, indent=4)
    print("\n Data saved to data.json.")

def load_data(filepath='data.json'):
    global user_data
    try:
        with open(filepath, 'r') as f:
            user_data.update(json.load(f))
        print(" Data loaded from data.json.")
    except FileNotFoundError:
        print(" No existing data found. Starting fresh.")
        print("Testing commit")
        print("Testing commit")