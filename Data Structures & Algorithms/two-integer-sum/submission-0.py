class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # no need to check nums length,
        # sort is necessary
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < len(nums) and j >= 0 and i < j:
            val = nums[i] + nums[j]
            if val == target:
                return [i,j]
            if val < target:
                i += 1
            elif val > target:
                j -= 1
        return []

