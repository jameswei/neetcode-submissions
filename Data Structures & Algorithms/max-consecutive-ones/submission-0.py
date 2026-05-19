class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        cur_max_count = 0
        count = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                cur_max_count = max(cur_max_count, count)
        
        cur_max_count = max(cur_max_count, count)
        return cur_max_count