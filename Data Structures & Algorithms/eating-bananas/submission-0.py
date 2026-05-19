class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        hour_per_pile = h // len(piles)
        return piles[-1]//hour_per_pile