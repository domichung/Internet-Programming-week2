from xmlrpc.server import SimpleXMLRPCServer
import create_thread as cth
import thread_show as ts
import thread_delete as td

PORT = 7788

def createthread(userid,tittle,info):
    print(userid,tittle,info)
    try:
        result_create = cth.addthread_tittle(tittle)
        result_post = cth.addthread(userid,tittle,info)
        if result_create != "success" or result_post != "success" :
            return "標題已經存在"
        else:
            return "發布成功"
    except:
        return "發布失敗"

def subject():
    re = ts.show_list()
    if (re == "未包含標題"):
        return -1
    else:
        return re 

def discussion(thread_num):
    return ts.show_info(thread_num)

def reply(account,tittle_id,comment):
    return (cth.addthread_intittleid(account,tittle_id,comment))

def get_mine_tittle(id):
    if (ts.show_list_user(id) == 'error'):
        return '妳尚未發布任何評論'
    else:
        return ts.show_list_user(id)

def delete_tittle(tittle):
    x = td.delete_check(tittle)
    print(x)
    if (x == 'faild'):
        return '不符合刪除條件'
    else:
        return '刪除成功!'
    
def main():
    server = SimpleXMLRPCServer(('localhost', PORT))
    
    server.register_function(createthread, 'createthread')
    server.register_function(subject, 'subject')
    server.register_function(discussion, 'discussion')
    server.register_function(reply, 'reply') 
    server.register_function(get_mine_tittle, 'get_mine_tittle')
    server.register_function(delete_tittle, 'delete_tittle')
    print('Listening on port %d' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
