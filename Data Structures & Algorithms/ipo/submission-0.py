class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        # 求k轮次后，w的最大值
        # 每一轮可选的project需要符合条件，capital[i]<=w，最优思路是选择可选project中profit最大的
        min_capital = []
        candidates = []

        for i in range(n):
            heapq.heappush(min_capital, (capital[i], i))

        while k > 0:
            
            while len(min_capital) > 0 and min_capital[0][0] <= w:
                cap, idx = heapq.heappop(min_capital)
                heapq.heappush(candidates, (-1*profits[idx], idx))

            if len(candidates) > 0:
                prof, idx = heapq.heappop(candidates)
                w += -1*prof
            
            k -= 1
        
        return w