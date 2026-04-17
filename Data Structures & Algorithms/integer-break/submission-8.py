class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] 数字i拆分后的最大乘积
        dp = [0] * (n+1)
        dp[1] = 1
        # 2至少拆分成2个数，只能是1,1，所以乘积只有1
        dp[2] = 1

        # dp[i] = max{j from 1 to i-1}(j*(i-j), j*dp[i-j])

        # 自底向上
        for i in range(3, n+1):
            # 这层循环的一样是题目要求至少拆成2个数，分别是j和i-j
            # 另外的原因是这道题的状态转移，并不是简单的从“前一个状态”直接得到，而是需要一次“决策”过程。
            for j in range(1, i):
                # max(只拆成j和i-j, 拆成j后继续递归拆i-j)
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])


        return dp[n]