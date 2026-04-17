class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_days = len(prices)
        
        hold = [0] * total_days
        just_sold = [0] * total_days
        wait_and_see = [0] * total_days

        hold[0] = -1*prices[0]
        just_sold[0] = -1*2**31
        wait_and_see[0] = 0

        # 从第二天开始
        for i in range(1, total_days):
            # price of ith day
            price = prices[i]

            hold[i] = max(hold[i-1], wait_and_see[i-1]+(-1*price))
            just_sold[i] = hold[i-1]+(1*price)
            wait_and_see[i] = max(wait_and_see[i-1], just_sold[i-1])

        max_profit = max(just_sold[total_days-1], wait_and_see[total_days-1])

        return max_profit