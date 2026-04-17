class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # subarray is a *contiguous sequence*
        # must no skip and keep original sequence
        # nums.sort()

        # dp[i] is largest sum of [...i] 
        # [2,-3,4,-2,2,1,-1,4]
        # [2,-1,4,2,4,5,4,8]

        # [-2,1,-3,4,-1,2,1,-5,4]
        # [-2,1,-2,4,3,5,6,1,5]
        dp = [0] * (len(nums))
        
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            largest_sum_by_now = dp[i-1]
            sum_include_num_i = largest_sum_by_now + num
            dp[i] = max(sum_include_num_i, num)

        return max(dp)