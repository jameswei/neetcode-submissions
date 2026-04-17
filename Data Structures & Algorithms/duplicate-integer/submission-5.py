class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        nums.sort()
        book = {nums[x]: 0 for x in range(len(nums))}
        for i in range(len(nums)):
            book[nums[i]] += 1
            if book[nums[i]] > 1:
                return True
        return False