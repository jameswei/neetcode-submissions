class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_days = len(prices)
        # 朴素想法：对于每一天结束时，存在多种状态：
        # 1.今天买入，持有
        # 2.之前买入，今天不卖，继续持有
        # 3.之前买入，今天卖出，空闲
        # 4.之前空闲，今天不买，继续空闲
        # 5.之前卖出，今天不买，继续空闲
        # 。。。

        # 以上的状态可能都对应微观上的区别，但是可以合并一些等价的状态！
        # 比如，不管今天前的操作是什么，只要今天结束时，空仓，那就是空闲状态，差别的只是盈利
        # 比如，不管今天前的操作是什么，只要今天结束是，持有股票，那就是持有状态
        # 按照这样合并，可能仅仅存在2种状态，持仓还是空仓！

        # 但是，今天内的操作，会对结果有影响。
        # 也就是今天的buy或sell，是2种状态转移的关键：
        # empty ---buy---> hold
        # hold ---sell---> empty
        # 此外，如果把休息 rest也当作一种操作的话，那再多两个，只不过前后状态是一样的
        # empty ---rest---> empty
        # hold ---rest---> hold
        
        # 状态合并后，只保留3种：
        # 空仓，可买
        # 空仓，不可买（题目要求的cooldown）
        # 持仓
        dp[i][0]
        dp = [[] * 3 for _ in range(total_days)]


        max_profit = 0
        return max_profit