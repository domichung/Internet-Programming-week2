import json
import os

filename = 'user_data.json'

def check_login(user, password):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_user in data.values():
        if existing_user['account'] == user:
            if existing_user['password'] == password:
                return "success"

    return "faild"