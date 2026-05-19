class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return false
        book = {nums[x]: 0 for x in range(len(nums))}
        for i in range(0, len(nums)):
            if book[nums[i]] > 1:
                return true
            book[nums[i]] += 1
        return false