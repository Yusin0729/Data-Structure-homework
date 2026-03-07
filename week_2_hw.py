import json
import os

user_account_data = "users.json"
if os.path.exists(user_account_data):
    with open(user_account_data, "r", encoding="utf-8") as f:
        user_data = json.load(f)
else:
    user_data = {}

while 1:
    user_choice = input("\n請選擇操作選項 (a 註冊, b 登入, c 退出) ？ ").strip().lower()

    if user_choice == "a":
        user_account = input("請輸入帳號 : ").strip()
        
        if user_account in user_data:
            print("帳號已存在，請重新輸入!")
        else:
            user_password = input("請輸入密碼 : ").strip()
            user_data[user_account] = user_password

            with open(user_account_data, "w", encoding="utf-8") as f:
                json.dump(user_data, f, ensure_ascii=False, indent=4)
                
            print("註冊成功！資料已儲存。")

    elif user_choice == "b":
        user_account = input("請輸入帳號 : ").strip()
        user_password = input("請輸入密碼 : ").strip()
        
        if user_account in user_data and user_data[user_account] == user_password:
            print("登入成功!")
        else:
            print("帳號或密碼錯誤，請重新登入!")

    elif user_choice == "c":
        print("系統已退出")
        break

    else:
        print("無效的選項，請輸入 a, b 或 c！")