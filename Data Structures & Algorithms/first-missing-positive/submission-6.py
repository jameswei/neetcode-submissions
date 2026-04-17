class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 找最小的没出现的正数
        nums.sort()
        min_val, max_val = nums[0], nums[-1]

        if min_val > 1 or max_val <= 0:
            return 1

        missing = 1
        for n in nums:
            if n <= 0:
                continue
            
            if n == missing:
                missing += 1

        return missing