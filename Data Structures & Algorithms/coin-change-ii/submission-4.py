class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp 解法
        coins.sort()

        # dp[i][j]，用[0,i)种硬币，凑出j 金额的方式
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1

        for i in range(1, len(dp)):
            coin = coins[i-1]

            for j in range(amount+1):

                if j == 0:
                    # 什么都不选，就能凑出0，这就是"一种"组合法
                    dp[i][j] = 1
                
                else:
                    dp[i][j] = dp[i-1][j] + (dp[i][j-coin] if j >= coin else 0)

        return dp[-1][-1]

                