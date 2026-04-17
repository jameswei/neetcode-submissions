class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # allowed to move only down or right
        # [0][0] -> [m][n]

        # [m-1][n] -> [m][n]
        # [m][n-1] -> [m][n]

        # dp[m][n] = dp[m-1][n] + dp[m][n-1]

        # m*n matrix
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(f"dp: {dp}")

        return dp[m-1][n-1]
