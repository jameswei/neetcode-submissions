class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # dfs解法
        n = len(arr)

        max_len = 1
        # 返回长度和上一对的波动关系
        def dfs(i: int) -> tuple[int, int]:
            nonlocal max_len
            if i == n-1:    
                # 边界时，把波动关系当作“值相等”，
                # 因为不存在上一对，用大小关系不能满足条件
                return (1, 0)

            cur_len, last_comp = dfs(i+1)

            if arr[i] == arr[i+1]:
                max_len = max(max_len, cur_len)
                return (1, 0)
            
            else:
                cur_comp = (arr[i] > arr[i+1]) - (arr[i] < arr[i+1])

                if cur_comp != last_comp:
                    max_len = max(max_len, cur_len)
                    return (cur_len+1, cur_comp)
                else:
                    max_len = max(max_len, cur_len)
                    return (2, cur_comp)

        dfs(0)
        return max_len