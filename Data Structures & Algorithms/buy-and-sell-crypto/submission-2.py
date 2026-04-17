class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            # no profit on a single day
            return 0
        
        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if price < lowest_price:
                lowest_price = price
            else:
                max_profit = max(max_profit, price - lowest_price)
        return max_profit