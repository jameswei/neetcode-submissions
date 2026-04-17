class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n =  len(arr)

        if n == 1:
            return 1

        # 1:a>b,-1:a<b,0:a==b
        def comp(a: int, b: int) -> int:
            return (a > b) - (a < b)

        last_comp = 0
        cur_len = max_len = 1

        for i in range(1, n):
            cur_comp = comp(arr[i], arr[i-1])
            
            if cur_comp != 0 and cur_comp != last_comp:
                cur_len += 1
                last_comp = cur_comp

            elif cur_comp == 0:
                max_len = max(max_len, cur_len)
                cur_len = 1
                last_comp = cur_comp

            else:
                max_len = max(max_len, cur_len)
                cur_len = 2
                last_comp = cur_comp
        

        # 别忘了遍历完之后的更新 
        max_len = max(max_len, cur_len)

        return max_len


        