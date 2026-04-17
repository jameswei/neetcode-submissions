class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = -2**31
        memo = [[INF] * 2 for _ in range(n)]

        # 朴素 dfs，将profit从参数中移除，
        # 这样才可以记忆化
        def dfs(i: int, hold: bool) -> int:
            if i == n:
                return 0

            if memo[i][1 if hold else 0] != INF:
                return memo[i][1 if hold else 0]

            profit = dfs(i+1, hold)

            if not hold:
                # 买
                profit = max(profit, -prices[i] + dfs(i+1, True))
            else:
                # 卖
                profit = max(profit, prices[i] + dfs(i+1, False))

            memo[i][1 if hold else 0] = profit
            
            return profit

        return dfs(0, False)

