class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        res = []
        n = len(nums)
        # heap 中是 tuple,由值的负数+索引组成，因为 heapq 只支持小顶堆
        heap = []

        for i in range(n):
            num = nums[i]
            heapq.heappush(heap, (num*-1, i))

            # len >= k
            # i-0+1 == k
            if i >= k-1:
                while len(heap) > 0 and heap[0][1] < i-k+1:
                    heapq.heappop(heap)
                
                res.append(heap[0][0]*-1)

            
        return res


