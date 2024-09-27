import json
import os
import time

def before_create_tittle(id):
    fname = "thread_data/" + str(id) + ".json"
    with open(fname, 'w', encoding='utf-8') as file:
        json.dump({}, file)

def add_tittle(filename,  thread_in_list):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_user in data.values():
        if existing_user['tittle'] ==  thread_in_list['tittle']:
            raise ValueError(f"Error: 標題 '{ thread_in_list['tittle']}' 已經存在!")

    if data:
        next_id = str(int(max(data.keys())) + 1)
    else:
        next_id = '1'  

    before_create_tittle(int(next_id))

    thread_in_list['id'] = next_id
    data[next_id] =  thread_in_list

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def addthread_tittle(tittle):
    filename = 'thread_list.json'
    thread_in_list = {
        'tittle':tittle
    }
    try:
        add_tittle(filename, thread_in_list)
        return "success"
    except ValueError as e:
        return e

#====================評論處理區=============================
def find_tittle(tittle):
    
    filename = 'thread_list.json'

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    i = 0

    for existing_user in data.values():
        if existing_user['tittle'] ==  tittle:
            return i+1
        i+=1
        
    return -1

def thread_in(filename,thread_data):
    if not os.path.exists(filename):
        raise ValueError(f"Error:'{filename}'不存在")

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    #for existing_user in data.values():
    #   continue 

    if data:
        next_id = str(int(max(data.keys())) + 1)
    else:
        next_id = '1'  

    thread_data['id'] = next_id
    data[next_id] =  thread_data

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
#======================================================
def addthread(account,tittle,comment):
        
    thread_data = {
        'account': account,
        'comment': comment,
        'time':time.localtime()
    }

    try:
        id = str(find_tittle(tittle))
        id += '.json'
        id = 'thread_data/' + id
        thread_in(id,thread_data)
        return "success"
    except ValueError as e:
        return e
    
def addthread_intittleid(account,tittle_id,comment):
        
    thread_data = {
        'account': account,
        'comment': comment,
        'time':time.localtime()
    }

    try:
        id = str(tittle_id)
        id += '.json'
        id = 'thread_data/' + id
        thread_in(id,thread_data)
        return "success"
    except ValueError as e:
        return e


#print(addthread_tittle("666"))
#print(find_tittle('666'))
#print(addthread('aaa','666','wawawa'))
#print(addthread_intittleid("wu","3","dog"))