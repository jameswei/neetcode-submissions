class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = 2**31-1
        dp = [INF] * len(nums)
        dp[-1] = 0

        for i in range(len(dp)-1, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j < len(dp):
                    dp[i] = min(dp[i], 1+dp[i+j])

        return dp[0]
