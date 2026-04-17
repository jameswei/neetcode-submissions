class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = 0
        for n in nums:
            total_sum += n

        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        dp = [[False] * (half_sum+1) for _ in range(len(nums)+1)]

        # target_sum == 0 时，天然满足
        for i in range(len(dp)):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for j in range(1, half_sum+1):
                dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i-1]] if j>=nums[i-1] else False)        

        return dp[len(nums)][half_sum]

