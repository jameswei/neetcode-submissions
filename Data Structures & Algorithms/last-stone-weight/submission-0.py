class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # choose 2 heaviest stones at each step
        negative_weights = [-x for x in stones]

        heapq.heapify(negative_weights)
        while len(negative_weights) > 1:
            heaviest = heapq.heappop(negative_weights) * -1
            heavier = heapq.heappop(negative_weights) * -1

            remains = (heaviest - heavier) * -1
            heapq.heappush(negative_weights, remains)
        
        return 0 if len(negative_weights) == 0 else negative_weights[0]*-1
