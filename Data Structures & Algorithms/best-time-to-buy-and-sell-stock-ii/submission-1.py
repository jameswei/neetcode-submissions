class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = -2**31

        # 记忆化+dfs
        def dfs(i: int, hold: bool, profit: int) -> int:

            if i == n:
                return profit

            price = prices[i]

            if not hold:
                # 买或者不动
                return max(dfs(i+1, True, (profit-price)),
                                dfs(i+1, False, profit))
            else:
                # 卖或者不动
                return max(dfs(i+1, False, (profit+price)),
                            dfs(i+1, True, profit))

        return dfs(0, False, 0)

