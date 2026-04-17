class Solution:
    # [5,1,2,10,6,2,7,9,3,1]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_amount = [0] * len(nums)
        max_amount[0] = nums[0]
        max_amount[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            max_amount[i] = max(nums[i]+max_amount[i-2], max_amount[i-1])

        return max_amount[len(nums)-1]