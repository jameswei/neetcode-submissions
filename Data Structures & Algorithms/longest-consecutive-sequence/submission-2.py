class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        
        longest = 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                length += 1
            if nums[i] - nums[i-1] > 1:
                longest = max(longest, length)
                length = 1
        longest = max(longest, length)
        return longest