import json
import os

def show_list():

    re = []

    filename = "thread_list.json"

    if not os.path.exists(filename):
        return "未包含標題"

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_user in data.values():
        re.append(existing_user['tittle']) 
    
    return re

def check_delete(id):
    filename = "thread_list.json"

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    #print(str(id) +"wwwwww")

    for existing_tittle in data.values():
        if existing_tittle['id'] == str(id):
            #print("cool2")
            if existing_tittle['tittle'] == '此篇以刪':
                #print("cool3")
                return 1

    #print(tittle+"tittlewwwwwwwwwwwwwwwwwwwwwwwwww")

    return 0

def show_info(id):

    print(id)
    if (check_delete(id) == 1):
        return "此篇以刪"

    re = []
    filename = "thread_data/" + str(id) + ".json"

    if not os.path.exists(filename):
        return "輸入錯誤"

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_info in data.values():
        re.append( existing_info['account']) 
        re.append( existing_info['time'])
        re.append( existing_info['comment'])
    return re

def show_list_user(user):

    re = []

    filename = "thread_list.json"

    if not os.path.exists(filename):
        return "未包含標題"

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_user in data.values():
        if (check_thread_mine(user,existing_user['id'])):
            re.append(existing_user['tittle'])
    
    if ( len(re) == 0 ):
        return 'error'
    else:
        return re

def check_thread_mine(user,artical_id):
    filename = "thread_data/" + str(artical_id) + ".json"
    
    if not os.path.exists(filename):
        return "未包含檔案"
    
    with open(filename,'r',encoding="utf-8") as file:
        data = json.load(file)
    
    #print(data)

    first_key = next(iter(data))
    #print(data[first_key]['account'])

    if (data[first_key]['account'] == user):
        return True
    else:
        return False
    

#print(show_list_user('5'))

#print(show_list())
#print(show_info(1))