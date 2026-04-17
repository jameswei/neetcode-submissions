class Solution:
    def numSquares(self, n: int) -> int:
        # 根据记忆化+dfs解法，得出dp解法

        dp = [2**31-1] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            j = 1

            while j**2 <= i:
                k = j**2
                dp[i] = min(dp[i], 1+dp[i-k])
                j += 1
                
        return dp[n]