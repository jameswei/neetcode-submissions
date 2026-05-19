class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # 单调增
        coins.sort()
        res = []
        memos = {}

        def dfs(i: int, remaining: int, path: list[int]):
            if remaining == 0:
                res.append(path[:])
                return

            if i > len(coins)-1:
                return
            
            val = coins[i]
            if val > remaining:
                return
                
            dfs(i, remaining-val, path)

            dfs(i+1, remaining, path)
            

        dfs(0, amount, [])
        return len(res)
