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

        def can_ship(cap: int) -> int:
            days_needed = 1
            total_weight = 0

            for w in weights:
                if total_weight + w > cap:
                    days_needed += 1
                    total_weight = 0
                total_weight += w
            return days_needed

        while l <= r:
            m = l+(r-l)//2

            required_days = can_ship(m)
            
            if required_days <= days:
                r = m - 1
            else:
                l = m + 1

        return l
        