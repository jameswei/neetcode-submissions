class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = -2**31

        memo = [[INF] * 2 for _ in range(n)]

        # 记忆化+dfs
        def dfs(i: int, hold: bool, profit: int) -> int:

            if i == n:
                return profit

            price = prices[i]

            if not hold:
                # 买或者不动
                memo[i][0] = max(dfs(i+1, True, (profit-price)),
                                dfs(i+1, False, profit))
            else:
                # 卖或者不动
                memo[i][1] = max(dfs(i+1, False, (profit+price)),
                            dfs(i+1, True, profit))

            return max(memo[i][0], memo[i][1])

        return dfs(0, False, 0)

