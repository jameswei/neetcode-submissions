class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 直觉思维是递归遍历所有拿法，如果给定piles多会超时，或者栈溢出
        # 结合游戏规则，其实是判断能否超过一半，因为最终石头被拿完，各自一半数量，两方分数等于所有石头的总分数
        # 如果先手的分数大于一半，肯定获胜

        # 对于当前的石头序列 piles[i], piles[i+1], ..., piles[j]，轮到当前玩家行动时，他最多能比对手多拿多少分？把这个“最大分数差”记作 dp[i][j]
        n = len(piles)
        dp = [[-1] * n for _ in range(n)]

        # dp对角线是初始状态，因为表示单个石头的序列[i]，因为先手，所以最大分数差就是这个石头分数
        for i in range(n):
            dp[i][i] = piles[i]

        # 按子序列长度递增来填dp表
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])

        return dp[0][n-1] > 0