class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 1 and len(text2) == 1:
            return 1 if text1[0] == text2[0] else 0 
        
        m, n = len(text1)+1, len(text2)+1

        # dp[i][j] == LCI of s[0:i] and t[0:j]
        dp = [[0] * m for _ in range(n)]
        # dp[0][] == 0 dp[][0] == 0

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = 0
                else:
                    if text1[j-1] == text2[i-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n-1][m-1]