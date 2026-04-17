class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 记忆化+dfs 转成 dp 解法
        # 递归函数，i,j,k，返回 bool
        # 递归条件是(i,j,k) = (i+1,j,k+1) or (i,j+1,k+1)
        m, n, o = len(s1), len(s2), len(s3)
        if m+n != o:
            return False
        
        dp = [[False] * (n+1) for _ in range(m+1)]
        # ""和""可以构成interleaving 的""
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s3[i+j] == s1[i] and dp[i+1][j]:
                    dp[i][j] = True
                if not dp[i][j] and j < n and s3[i+j] == s2[j] and dp[i][j+1]:
                    dp[i][j] = True

        return dp[0][0]
