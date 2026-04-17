class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False
            
            max_steps = nums[i]

            furthest_from_here = i + max_steps
            if furthest_from_here >= len(nums)-1:
                return True

            furthest = max(furthest, furthest_from_here)

        return False