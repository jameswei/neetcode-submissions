class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 找最小的没出现的正数
        nums.sort()
        min_val, max_val = nums[0], nums[-1]

        if min_val > 1 or max_val <= 0:
            return 1

        start = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                continue
            
            if nums[i] != start+1:
                return start+1

            start += 1



        return max_val+1