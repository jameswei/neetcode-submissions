class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # no need to check nums length, neither sorting
        for i in range(len(nums)-1):
            for j in range (i + 1, len(nums)):
                val = nums[i] + nums[j]
                if val == target:
                    return [i, j]
        return []

