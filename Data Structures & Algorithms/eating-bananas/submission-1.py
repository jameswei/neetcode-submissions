class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_bananas_per_hour = 1
        max_bananas_per_hour = max(piles)

        # eating rate must in [min_banans_per_hour, max_bananas_per_hour]
        while min_bananas_per_hour < max_bananas_per_hour:
            mid = min_bananas_per_hour+(max_bananas_per_hour-min_bananas_per_hour)//2
            # if mid rate can eat up all bananas, move min up
            # else move max down
            total_hours = 0
            for num in piles:
                total_hours += math.ceil(num/mid)
            
            if total_hours <= h:
                max_bananas_per_hour = mid
            else:
                min_bananas_per_hour = mid+1
            
        return min_bananas_per_hour