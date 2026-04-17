class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_days = len(prices)

        max_profit = 0
        def dfs(day: int, hold_price: int, can_buy: bool, profit: int):
            nonlocal max_profit
            if day >= total_days:
                max_profit = max(max_profit, profit)
                return

            price = prices[day]

            if hold_price == -1 :
                if not can_buy:
                    # 啥也干不了
                    return
                
                # 买或者不买
                dfs(day+1, price, False, profit+0)

                dfs(day+1, -1, True, profit+0)
            
            # 继续 hold 不卖或者卖
            else:
                dfs(day+1, hold_price, False, profit+0)

                new_profit = profit + (price-hold_price)
                # 有 cooldown，要空一天
                dfs(day+2, -1, True, new_profit)

        dfs(0, -1, True, 0)
        return max_profit

