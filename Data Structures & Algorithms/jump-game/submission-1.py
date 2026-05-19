class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True

        # [2,5,0,0]
        # [t,t,f,t]
        dp = [False] * len(nums)
        # 已经在终点
        dp[len(nums)-1] = True

        for i in range (len(nums)-2, -1, -1):
            furthest = nums[i]
            can_jump_to_end_directly = (i+furthest)>=(len(nums)-1)
            can_jump_to_end_indirectly = False
            for j in range(furthest+1):
                can_jump_to_end_indirectly = can_jump_to_end_directly or dp[i+j]
            
            dp[i] = can_jump_to_end_directly or can_jump_to_end_indirectly

        return dp[0]