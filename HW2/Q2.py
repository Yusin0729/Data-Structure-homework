import time
from collections import deque

# --- 作業準備：建立 30 萬筆排隊資料 ---
print("正在建立 30 萬人的排隊系統，請稍候...")
queue_size = 300000
python_list_queue = list(range(queue_size))
linked_list_queue = deque(range(queue_size))
print("系統建立完畢！\n" + "-"*30)

# ==========================================
# 測試 4：VIP 頭部插隊
# ==========================================
print("【測試 1：1000 位 VIP 進入隊伍最前面】")
insert_count = 1000

# 4-1. Python List 頭部插隊
start_time = time.time()
for i in range(insert_count):
    # TODO 4-1 完成：用 .insert(0, ...) 插入最前面
    python_list_queue.insert(0, "VIP")

end_time = time.time()
print(f"Python List (O(N) 平移) 耗時: {end_time - start_time:.5f} 秒")

# 4-2. Deque 頭部插隊
start_time = time.time()
for i in range(insert_count):
    # TODO 4-2 完成：用 .appendleft() 插入最前面
    linked_list_queue.appendleft("VIP")

end_time = time.time()
print(f"Deque (O(1) 瞬間牽手) 耗時: {end_time - start_time:.5f} 秒")
print("-" * 30)

# ==========================================
# 測試 5：行銷部抽獎 (Random Access)
# ==========================================
print("【測試 2：行銷部隨機查詢第 15 萬號排隊者 1000 次】")
target_index = 150000
query_count = 1000

# 5-1. Python List 隨機存取
start_time = time.time()
for _ in range(query_count):
    # TODO 5-1 完成：直接用 [] 取值
    lucky_guy = python_list_queue[target_index]

end_time = time.time()
print(f"Python List (O(1)) 耗時: {end_time - start_time:.5f} 秒")

# 5-2. Deque 隨機存取
start_time = time.time()
for _ in range(query_count):
    # TODO 5-2 完成：直接用 [] 取值
    lucky_guy = linked_list_queue[target_index]

end_time = time.time()
print(f"Deque (O(N) 從頭慢慢找) 耗時: {end_time - start_time:.5f} 秒")

# ==========================================
# 問題 6：觀念解釋
# ==========================================

# 6-1. 為什麼 4-1 和 4-2 差這麼多，底層是什麼原因？
#
#   【Python List - 慢的原因：O(N) 平移】
#   Python List 底層是連續記憶體的 Array。
#   在 index 0 插入資料，代表原本的每一筆資料都要往後移動一格，
#   才能空出第一個位置給新來的 VIP。
#
#   記憶體示意：
#   插入前：[0][1][2]...[299999]
#   插入後：[VIP][0][1][2]...[299999]
#                ← 全部 30 萬筆資料向右平移
#
#   每次插入 = O(N)，做 1000 次 = O(1000N) = 搬動約 3 億筆，非常慢。
#
#   【Deque - 快的原因：O(1) 改指標】
#   deque 底層是 Doubly Linked List（雙向鏈結串列）。
#   每個節點存著「前一個」和「後一個」的指標，不需要住在連續記憶體。
#
#   插入新節點到最前面，只需要：
#     ① 新節點的 next 指向舊的第一個節點
#     ② 舊的第一個節點的 prev 指向新節點
#     ③ HEAD 指向新節點
#   只改 3 條指標，跟隊伍有多長完全無關 = O(1)
#
#   結論：頭部插入這件事，Array 的連續記憶體反而是缺點，
#         Linked List 的指標結構才是優勢。


# 6-2. 為什麼 5-1 和 5-2 差這麼多，底層是什麼原因？
#
#   【Python List - 快的原因：O(1) 隨機存取】
#   Array 的連續記憶體讓 CPU 可以用公式直接計算任意位置的地址：
#
#     目標地址 = 起始地址 + (index × 每個元素的大小)
#
#   不管要找第 1 個還是第 150000 個，都是同一條算式，一步到位。
#   這就叫做「隨機存取（Random Access）」= O(1)
#
#   【Deque - 慢的原因：O(N) 循序存取】
#   Linked List 的節點散落在記憶體各處，彼此只靠指標連接。
#   因為沒有「起始地址 + 位移」這種公式可用，
#   要找第 150000 個節點，只能從 HEAD 開始，
#   一步一步跟著指標走，走到第 150000 步才能找到。
#
#   這叫做「循序存取（Sequential Access）」= O(N)
#   index 越大，要走的路越長，查詢越慢。
#
# 結論
# 隨機存取這件事，Array 的連續記憶體是最大優勢，
# Linked List 的指標結構反而是致命缺點。