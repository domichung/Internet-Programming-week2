import json
import os

def delete_check(tittle):
    check = tittle_to_id(tittle)
    if (check == 'faild'):
        return 'faild'
    else:
         f_name = "thread_data/" + str(check) + ".json"

    if not os.path.exists(f_name):
        return 'faild'

    with open(f_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    commentcounter = 0

    for existing_tittle in data.values():
        commentcounter+=1

    if (commentcounter > 2):
        return 'faild'
    else:
        del_sys(check)

def del_sys(thread_id):
    filename = "thread_list.json"
    deleted_log_file = "delete_log.json"

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Error: 檔案 '{filename}' 不存在！")

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    found = False
    deleted_id = None

    # 查找並替換匹配的標題和ID
    for key, existing_user in data.items():
        if existing_user['id'] == thread_id:
            deleted_id = key  # 保存被替換的id
            existing_user['tittle'] = "此篇以刪"
            existing_user['id'] = existing_user['id']
            found = True
            break

    if not found:
        raise ValueError(f"Error: 標題 '{thread_id}' 不存在，無法替換！")

    # 將被替換的id寫入到指定的log檔案
    if deleted_id:
        if not os.path.exists(deleted_log_file):
            with open(deleted_log_file, 'w', encoding='utf-8') as log_file:
                json.dump([], log_file)

        with open(deleted_log_file, 'r+', encoding='utf-8') as log_file:
            deleted_log = json.load(log_file)
            deleted_log.append(deleted_id)
            log_file.seek(0)
            json.dump(deleted_log, log_file, ensure_ascii=False, indent=4)

    # 更新主文件，保存修改
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return "success"

def tittle_to_id(tittle):

    filename = "thread_list.json"

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for existing_tittle in data.values():
        if existing_tittle['tittle'] ==  tittle:
            return existing_tittle['id']

    #print(tittle+"tittlewwwwwwwwwwwwwwwwwwwwwwwwww")

    return "faild"

#print(delete_check("1"))