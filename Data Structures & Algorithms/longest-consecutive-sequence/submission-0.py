class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        longest = 0
        length = 1
        i, j = 0, 1
        while j < len(nums):
            if nums[j] - nums[j-1] > 1:
                i = j
                longest = max(longest, length)
            elif nums[j] - nums[j-1] == 1:
                length += 1
            j += 1
        longest = max(longest, length)
        return longest