import json
import os

def append_user_data(filename, user_data):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_user in data.values():
        if existing_user['account'] == user_data['account']:
            raise ValueError(f"Error: 帳號 '{user_data['account']}' 已經存在!")

    if data:
        next_id = str(int(max(data.keys())) + 1)
    else:
        next_id = '1'  

    user_data['id'] = next_id
    data[next_id] = user_data

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def addaccount(input_account,input_password):
    filename = 'user_data.json'
    new_user_data = {
        'account': input_account,
        'password': input_password
    }
    try:
        append_user_data(filename, new_user_data)
        return "success"
    except ValueError as e:
        return e
    

#print(addaccount('b','baba'))