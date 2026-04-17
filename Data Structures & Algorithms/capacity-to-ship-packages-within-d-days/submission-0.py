class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 重要的思路：
        # 船的运载能力的下限，至少要大于等于最重的包裹，否则无法运输
        # 运载能力的上限，所有包裹的重量综合，一次就运完
        # 题目要求找least capacity，也就是最小可行的运载能力，那就是不断缩小的过程
        # 二分查找应该可以试试
        min_capacity = max(weights)
        max_capacity = sum(weights)
        INF = 2**31-1

        l, r = min_capacity, max_capacity

        while l <= r:
            m = l+(r-l)//2
            
            total_weights = 0
            total_days = 0

            for w in weights:
                total_weights += w

                if total_weights > m:
                    total_days += 1
                    total_weights = w

            total_days += INF if total_weights > m else 1
            
            if total_days <= days:
                r = m - 1
            else:
                l = m + 1

        return l
        