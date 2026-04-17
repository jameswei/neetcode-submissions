class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp 解法
        coins.sort()

        # dp[i][j]，用[0,i)种硬币，凑出j 金额的方式
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 1

        for i in range(1, len(dp)):
            coin = coins[i-1]

            for j in range(amount+1):
                dp[i][j] = dp[i-1][j]

                if j >= coin:
                    dp[i][j] += dp[i][j-coin]

        return dp[len(coins)][amount]

                