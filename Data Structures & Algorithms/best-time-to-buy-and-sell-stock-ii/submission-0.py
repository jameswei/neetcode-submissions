class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 其实求可能的最大值，应该初始化成-INF
        max_profit = 0

        def dfs(i: int, hold: bool, profit: int):
            nonlocal max_profit

            if i > n-1:
                max_profit = max(max_profit, profit)
                return

            price = prices[i]

            if not hold:
                # 买或者不动
                dfs(i+1, True, profit-price)

                dfs(i+1, False, profit)

            else:
                # 卖或者不动
                dfs(i+1, False, profit+price)

                dfs(i+1, True, profit)

        dfs(0, False, 0)

        return max_profit

