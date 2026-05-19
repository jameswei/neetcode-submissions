class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return n
        
        left = 0
        max_len = 1
        
        for right in range(1, n):
            # 判断当前比较与前一个比较的关系
            if right == 1 or (arr[right] - arr[right-1]) * (arr[right-1] - arr[right-2]) < 0:
                # 符号交替
                max_len = max(max_len, right - left + 1)
            elif arr[right] == arr[right-1]:
                # 值相等
                max_len = max(max_len, right - left)
                left = right
            else:
                # 符号相同
                max_len = max(max_len, right - left)
                left = right - 1
        
        return max_len