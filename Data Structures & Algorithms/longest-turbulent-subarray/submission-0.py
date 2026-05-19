class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 问题本质“最长子串”，只不过子串的条件是数值满足交替波动
        # 根据题目给定的“波动”概念，邻接的pair的差值应该是正负交替
        # 所以根据长度为n的arr来计算每个邻接pair的差值，应该得到长度为n-1的差值列表
        # 接着可以在差值列表上来寻找最长子串，最终结果+1
        n =  len(arr)
        
        # 符号列表，根据相邻pair的差值得出符号，理想情况下因为符号相反，乘积应为负数
        diff_arr = [0] * (n-1)
        for i in range(1, n):
            diff_arr[i-1] = -1 if arr[i-1]<arr[i] else 1

        # 滑动窗口解法
        # [i,j)
        i, j = 0, 0
        product_in_window = 1
        max_len = 0

        while j < n-1:
            # 扩大窗口
            j += 1
            new_val = diff_arr[j-1]

            # 检查窗口
            if j-1 == 0 or new_val*product_in_window < 0:
                product_in_window *= new_val
                max_len = max(max_len, j-i)

            # 缩小窗口
            else:
                i = j - 1
                product_in_window = new_val

        return max_len
        