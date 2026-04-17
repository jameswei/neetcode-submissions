class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] 数字i拆分后的最大乘积
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        # dp[i] = max{j from 1 to i-1}(j*(i-j), j*dp[i-j])

        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])


        return dp[n]