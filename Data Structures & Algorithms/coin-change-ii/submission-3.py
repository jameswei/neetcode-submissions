class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 保证单调增
        coins.sort()
        # {(i,remaining): num_of_combinations}
        memo = {}

        def dfs(i: int, remaining: int) -> int:
            if remaining == 0:
                return 1

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            ans = 0
            for j in range(i, len(coins)):
                val = coins[j]

                if val > remaining:
                    break
                
                ans += dfs(j, remaining-val)

            memo[(i, remaining)] = ans
            
            return ans

        return dfs(0, amount)
