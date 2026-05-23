#暴力解
def twoSumBruteForce(nums, target):
    n = len(nums)
    # 第一層迴圈：遍歷每一個數字
    for i in range(n):
        # 第二層迴圈：從 i 的下一個數字開始往後找
        for j in range(i + 1, n):
            # 如果兩個數字相加等於目標值，直接回傳索引
            if nums[i] + nums[j] == target:
                return [i, j]

# 測試
nums = [2, 7, 11, 15]
target = 9
print(f"暴力解結果: {twoSumBruteForce(nums, target)}") # 輸出: [0, 1]

#效率解
def twoSumEfficient(nums, target):
    # 建立一個字典，用來記錄 {看過的數字: 它的索引}
    hashmap = {}
    
    # 使用 enumerate 同時取得索引 (i) 與數值 (num)
    for i, num in enumerate(nums):
        # 計算我需要的「補數」是多少
        complement = target - num
        
        # 檢查這個補數是否已經在我們的字典裡了
        if complement in hashmap:
            # 如果有，回傳 [補數的索引, 現在的索引]
            return [hashmap[complement], i]
        
        # 如果沒找到，就把現在這個數字存進字典，等後面的人來找它
        hashmap[num] = i

# 測試
print(f"效率解結果: {twoSumEfficient(nums, target)}") # 輸出: [0, 1]