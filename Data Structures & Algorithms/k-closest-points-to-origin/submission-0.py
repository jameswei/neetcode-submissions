class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap by distance to [0,0]
        distance_to_origin = []

        for point in points:
            x, y = point[0], point[1]
            d = math.sqrt(x**2+y**2)
            distance_to_origin.append((d, (x, y)))

        heapq.heapify(distance_to_origin)
        res = []
        while k > 0:
            (d, p) = heapq.heappop(distance_to_origin)
            res.append(list(p))
            k -= 1
        
        return res