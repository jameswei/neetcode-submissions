class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i]是从[i]台阶迈步的代价
        # 从任意台阶[i]既可以走一步，也可以两步
        # 那么到达最高层台阶[n-1]的代价就是：
        # 从[n-1-1]迈步的代价或者从[n-1-2]迈步的代价，取二者最小者
        # 以此类推，整个上台阶过程都选择最小代价，最终的和就是总路程的最小代价

        # dp[i] 就是到达[i]花费的最小代价
        dp = [0] * (len(cost)+1)
        # 允许从[0]或[1]起步，所以达到这两级台阶没有代价
        dp[0], dp[1] = 0, 0

        # 从 [2] 开始算
        for i in range(2, len(dp)):
            # from -1 floor
            cost1 = dp[i-1]+cost[i-1]

            # from -2 floor
            cost2 = dp[i-2]+cost[i-2]

            dp[i] = min(cost1, cost2)

        return dp[-1]