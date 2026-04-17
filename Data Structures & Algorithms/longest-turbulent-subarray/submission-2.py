class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 问题本质“最长子串”，只不过子串的条件是数值满足交替波动
        # 根据题目给定的“波动”概念，邻接的pair的差值应该是正负交替
        # 所以根据长度为n的arr来计算每个邻接pair的差值，应该得到长度为n-1的差值列表
        # 接着可以在差值列表上来寻找最长子串，最终结果+1
        n =  len(arr)
        
        # 归一化的差值列表，根据相邻pair的差值得出±1，最长子串的和应为0
        diff_arr = [0] * (n-1)
        for i in range(1, n):
            # 要求严格的差值，相等的情况也是不满足条件
            if arr[i-1] == arr[i]:
                diff_arr[i-1] = 0
            else:
                diff_arr[i-1] = (arr[i-1] - arr[i]) // abs(arr[i-1]-arr[i])

        print(f"diff_arr: {diff_arr}")

        # 滑动窗口解法
        # [i,j)
        i, j = 0, 0
        max_len = 0
        prev_val = 0
        while j < n-1:
            # 扩大窗口
            j += 1
            new_val = diff_arr[j-1]
            prev_val = diff_arr[j-2] if j>i+1 else 0

            print(f"i: {i}, j: {j}, new_val: {new_val}, prev_val: {prev_val}")

            # 检查窗口
            if new_val != 0 and (prev_val == 0 or new_val ^ prev_val < 0):
                max_len = max(max_len, j-i)
            
            # 缩小窗口
            elif new_val == 0:
                i = j
            else:
                i = j - 1

            print(f"i: {i}, j: {j}")

        return max_len+1
        