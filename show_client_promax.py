import sys
import os
import xmlrpc.client

PORT = 7788

def user_sys(userid):

    server = xmlrpc.client.ServerProxy('http://' + "127.0.0.1" + ':' + str(PORT))

    os.system("cls")
    print("歡迎使用者 %s\n請選擇功能:\n1. 創建新討論串\n2. 新增評論\n3. 查詢討論串\n4. 刪除討論串\nexit 離開" %userid)
    choose = input()
    match choose:
        case "1":
            print("輸入新增主題名稱:")
            tittle = input()
            print("輸入內文")
            info = input()
            result = server.createthread(userid,tittle,info)
            print(result)
        case "2":
            result = server.subject()
        
            while (1):

                w = 1
                os.system("cls")
                print("=======目前討論主題========")

                if (result == -1):
                    print("暫時不存在討論主題")
                    exit(0)

                for i in result:
                    print(str(w) + " " + i)
                    w+=1
            
                w-=2

                print("===========================")

                print("請輸入 想觀看的主題編號:")
                
                try:
                    show_tittle = int(input()) - 1
                except:
                    os.system("cls")
                    print("錯誤的輸入請重新輸入!")
                    input()

                #print(str(w)+" "+str(show_tittle))
                try:
                    if (show_tittle>w):
                        os.system("cls")
                        print("錯誤的輸入請重新輸入!")
                        input()
                    else:
                        os.system("cls")
                        break
                except:
                    os.system("cls")
                    print("錯誤的輸入請重新輸入!")
                    input()

            print("標題 : " + result[show_tittle])
            print("=============================")
            print("主樓:")
            get_thread_info = server.discussion(int(show_tittle)+1)

            if (get_thread_info == "此篇以刪"):
                os.system("cls")
                print("此篇以刪")
                input()
                return 1

            flag = 1

            for i in get_thread_info :
                match (flag%3):
                    case 1:
                        print("  用戶 : ",end="")
                    case 2:
                        print("  於",end="")
                    case 0:
                        print("  提出評論 : ",end="")
                print(i)
                if (flag%3 == 0):
                    print("=============================")
                flag +=1
            
            print("發表回應:")
            req = input()
            #print(show_tittle)
            req_check = server.reply(userid,show_tittle+1,req)
            print(req_check)

        case "3":
            result = server.subject()
            
            while (1):

                w = 1
                os.system("cls")
                print("=======目前討論主題==========")

                if (result == -1):
                    print("暫時不存在討論主題")
                    exit(0)

                for i in result:
                    print(str(w) + " " + i)
                    w+=1
            
                print("=============================")
                
                w-=2

                print("請輸入 想觀看的主題編號:")

                try:
                    show_tittle = int(input()) - 1
                except:
                    os.system("cls")
                    print("錯誤的輸入請重新輸入!")
                    input()

                #print(str(w)+" "+str(show_tittle))
                try:
                    if (show_tittle>w):
                        os.system("cls")
                        print("錯誤的輸入請重新輸入!")
                        input()
                    else:
                        os.system("cls")
                        break
                except:
                    print("錯誤的輸入請重新輸入!")
                    input()

            print("標題 : " + result[show_tittle])
            print("=============================")
            print("主樓:")
            get_thread_info = server.discussion(int(show_tittle)+1)
            if (get_thread_info == "此篇以刪"):
                os.system("cls")
                print("此篇以刪")
                input()
                return 1

            flag = 1

            for i in get_thread_info :
                match (flag%3):
                    case 1:
                        print("  用戶 : ",end="")
                    case 2:
                        print("  於",end="")
                    case 0:
                        print("  提出評論 : ",end="")
                print(i)
                if (flag%3 == 0):
                    print("=============================")
                flag +=1
        
            input()
        case "4":
            os.system("cls")
            print("=======妳的討論主題==========")
            get_mine_thread = server.get_mine_tittle(userid)
            counter = 1
            for i in get_mine_thread:
                print(str(counter) + " " + i)
                counter+=1
            print("=============================\n請輸入想刪除的主題\n注意超過一則評論則無法刪除")
            willdel = input()
            #print(get_mine_thread[int(willdel)-1])
            #input()
            try:
                check_del = server.delete_tittle(get_mine_thread[int(willdel)-1])
                print(check_del)
                input()
            except:
                os.system("cls")
                print("錯誤的輸入")
                input()
        case "exit":
            return -1
        case _:
            print("error input")
            input()



#user_sys('domi')