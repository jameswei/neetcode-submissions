class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            # no profit on a single day
            return 0
        
        max_profit = 0
        # no need to buy at the same price
        memo = set()

        i = 0
        while i < len(prices) - 1:
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
            # either j == len(prices) or prices[j] <= prices[i]
            if j == len(prices):
                i += 1
            else:
                i = j
        return max_profit