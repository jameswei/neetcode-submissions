class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return n
        
        left = 0
        max_len = 1
        
        for right in range(1, n):
            # 必须优先判断值是否相等的情况。
            # 因为如果给定arr长度为2，只会for循环一次，如果进入right==1的豁免分支，就会错误的更新长度
            if arr[right] == arr[right-1]:
                # 值相等
                left = right
            elif right == 1 or (arr[right] > arr[right-1]) != (arr[right-1] > arr[right-2]):
                # 符号交替
                max_len = max(max_len, right - left + 1)
            else:
                # 符号相同
                left = right - 1
        
        return max_len