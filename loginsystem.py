user_data = {}

while True:
    user_choice = input("請選擇操作選項 (a 註冊, b 登入, c 退出) ？ ")

    if user_choice == "a" or "A":
        user_account = input("請輸入帳號 : ")
        
        if user_account in user_data:
            print("帳號已存在，請重新輸入!")
        else:
            user_password = input("請輸入密碼 : ")
            user_data[user_account] = user_password
            print("註冊成功!")

    elif user_choice == "b" or "b":
        user_account = input("請輸入帳號 : ")
        user_password = input("請輸入密碼 : ")
        
        if user_account in user_data and user_data[user_account] == user_password:
            print("登入成功!")
        else:
            print("帳號或密碼錯誤，請重新登入!")

    elif user_choice == "c" or "C":
        print("系統已退出")
        break

    else:
        print("無效的選項，請輸入 a, b 或 c！")