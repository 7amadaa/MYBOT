import json
import os

DATA_FILE = 'user_data.json'

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # If there's an error, return an empty dictionary
                return {}
    return {}

def save_user_data(user_data):
    with open(DATA_FILE, 'w') as f:
        json.dump(user_data, f, indent=4)

def add_user(user_id, username):
    user_data = load_user_data()
    user_data[user_id] = username
    save_user_data(user_data)

def remove_user(user_id):
    user_data = load_user_data()
    if user_id in user_data:
        del user_data[user_id]
        save_user_data(user_data)

def get_username(user_id):
    user_data = load_user_data()
    return user_data.get(user_id, f"User with ID {user_id}")
