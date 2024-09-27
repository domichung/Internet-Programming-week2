import sys
import xmlrpc.client
import show_client_promax as scp
import os

PORT = 8888

def main():

    if (len(sys.argv) < 2):
        print("請於後面接上連線ip")
        exit(1)

    server = xmlrpc.client.ServerProxy('http://' + sys.argv[1] + ':' + str(PORT))
    while (1):
        os.system("cls")
        print("======指令表=======\n1. 註冊帳號\n2. 登入系統\nexit 離開系統")
        choose = input()
        match choose:
            case "1":
                print("輸入帳號")
                account = input()
                print("輸入密碼")
                password = input()
                result = server.register(account, password)
                print(result)            
                input()
            case "2":
                print("輸入帳號")
                account = input()
                print("輸入密碼")
                password = input()
                result = server.login(account, password)
                print(result)
                if (result == '登入成功'):
                    while(1):
                        leave = scp.user_sys(account)
                        if (leave == -1):
                            break
                else:
                    input()
            case "exit":
                break
            case _:
                print("error input")

if __name__ == '__main__':
    main()