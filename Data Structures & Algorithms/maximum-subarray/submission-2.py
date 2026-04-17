class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        largest_sum = float('-inf')
        cur_sum = float('-inf')

        for i in range(len(nums)):
            num = nums[i]
            if cur_sum + num <= num:
                cur_sum = num
            else:
                cur_sum += num

            largest_sum = max(largest_sum, cur_sum)

        return int(largest_sum)