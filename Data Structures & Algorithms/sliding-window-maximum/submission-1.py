class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        res = []
        n = len(nums)
        # [i,j)
        i, j = 0, 0
        
        while j < n:
            num = nums[j]
            j += 1

            if j-i < k:
                continue
            
            if j-i == k:
                res.extend(heapq.nlargest(1, nums[i:j]))

            if j-i > k:
                i += 1
                res.extend(heapq.nlargest(1, nums[i:j]))
        
        return res


