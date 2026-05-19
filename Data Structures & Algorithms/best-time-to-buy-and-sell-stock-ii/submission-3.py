class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = -2**31

        # 朴素 dfs
        # At each day, we have a choice: 
        # if we are not holding stock, we can either buy or skip. 
        # If we are holding stock, we can either sell or skip. 
        # We want to maximize profit by trying all possible buy and sell decisions.
        def dfs(i: int, hold: bool) -> int:
            if i == n:
                return 0

            profit = dfs(i+1, hold)

            if not hold:
                # 买
                profit = max(profit, -prices[i] + dfs(i+1, True))
            else:
                # 卖
                profit = max(profit, prices[i] + dfs(i+1, False))

            return profit

        return dfs(0, False)

