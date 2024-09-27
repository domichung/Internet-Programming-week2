from xmlrpc.server import SimpleXMLRPCServer
import account_create as acc
import check_account as cac
import threading

PORT = 8888

lock = threading.Lock()

def register(account, password):
    lock.acquire()
    try:
        result = acc.addaccount(account, password)
        if result != "success":
            return "帳號 " + account + " 已經存在"
        else:
            return "註冊成功"
    finally:
        lock.release()

def login(account, password):
    lock.acquire()
    try:
        result = cac.check_login(account, password)
        if result != "success":
            return "登入失敗"
        else:
            return "登入成功"
    finally:
        lock.release()

def main():
    server = SimpleXMLRPCServer(('localhost', PORT))

    server.register_function(register, 'register')
    server.register_function(login, 'login')

    print('Listening on port %d' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
