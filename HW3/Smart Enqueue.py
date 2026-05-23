from collections import deque

# 初始環境設定
player_gold = 150
barracks_A = deque()
barracks_B = deque()
MAX_CAPACITY = 2 

orders = [
    {"unit": "劍士", "cost": 20},    # 第 0 回合
    {"unit": "弓手", "cost": 30},    # 第 1 回合
    {"unit": "騎士", "cost": 50},    # 第 2 回合
    {"unit": "投石車", "cost": 40},  # 第 3 回合
    {},                             # 第 4 回合
    {"unit": "巨龍", "cost": 500}   # 第 5 回合
]

for round_num, order in enumerate(orders, start=0):
    print(f"\n--- 第 {round_num} 回合 ---")

    # Dequeue 邏輯
    if round_num % 2 == 0:
        if barracks_A:
            finished = barracks_A.popleft()
            print(f"A 廠生產完成：{finished}")
        else:
            print("A 廠沒東西可做 (Underflow 防護成功)")
            
        if barracks_B:
            finished = barracks_B.popleft()
            print(f"B 廠生產完成：{finished}")
        else:
            print("B 廠沒東西可做 (Underflow 防護成功)")

    # Enqueue 邏輯
    if not order:
        if round_num % 2 == 0:
            print("玩家本回合無動作，單純推進時間")
    else:
        unit = order.get("unit")
        cost = order.get("cost")

        if player_gold < cost:
            print(f"黃金不足，無法生產 {unit}")
        elif len(barracks_A) >= MAX_CAPACITY and len(barracks_B) >= MAX_CAPACITY:
            print(f"產線全滿！{unit} 訂單拒絕")
        else:
            if len(barracks_A) <= len(barracks_B) and len(barracks_A) < MAX_CAPACITY:
                barracks_A.append(unit)
                player_gold -= cost
                print(f"{unit} 分派至 A 廠 (剩餘黃金: {player_gold})")
            elif len(barracks_B) < MAX_CAPACITY:
                barracks_B.append(unit)
                player_gold -= cost
                print(f"{unit} 分派至 B 廠 (剩餘黃金: {player_gold})")

    print(f"A: {list(barracks_A)} | B: {list(barracks_B)}")