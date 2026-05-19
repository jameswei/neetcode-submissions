class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # 单调增
        coins.sort()

        def dfs(i: int, remaining: int) -> int:
            print(f"i: {i}, remaining: {remaining}")
            if remaining == 0:
                return 1

            ans = 0

            for j in range(i, len(coins)):
                val = coins[j]

                if val > remaining:
                    break
                
                ans += dfs(j, remaining-val)        
            
            return ans

        return dfs(0, amount)
        
