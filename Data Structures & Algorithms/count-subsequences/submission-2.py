class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 将记忆化+ dfs 的解法改为dp 的解法
        m, n = len(s), len(t)
        # 区别于记忆化+dfs 中的 memo 定义
        # dp[i][j]，s[0...i-1] 和 t[0..j-1]的范围内满足条件的数量
        dp = [[-1] * (n+1) for _ in range(m+1)]
        # 初始化状态也和递归函数中的 base-case 不同
        # 本质上能对应上，但是“方向”相反
        # s是空字符串的情况下，无法找到和t 相同的子序列（0种）
        dp[0] = [0] * (n+1)
        # t是空字符串的情况下，t 只需要不选择任何字符，就成为1种和t 相同的子序列
        for r in range(m+1):
            dp[r][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]