class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_amount = 0
        for i in range(0, 2):
            amount = 0
            for j in range(i, len(nums), 2):
                amount += nums[j]
            max_amount = max(max_amount, amount)
        
        return max_amount