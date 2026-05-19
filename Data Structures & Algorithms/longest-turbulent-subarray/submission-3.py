class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n =  len(arr)

        if n == 1:
            return 1

        cur_len = max_len = 1

        for i in range(1, n):
            cur_num = arr[i]
            prev_num = arr[i-1]

            if cur_num < prev_num and (i < 2 or arr[i-2] > cur_num):
                cur_len += 1
            elif cur_num > prev_num and (i < 2 or arr[i-2] < cur_num):
                cur_len += 1

            elif cur_num == prev_num:
                max_len = max(max_len, cur_len)
                cur_len = 1
            else:
                max_len = max(max_len, cur_len)
                curl_len = 2

            
        return max_len+1


        