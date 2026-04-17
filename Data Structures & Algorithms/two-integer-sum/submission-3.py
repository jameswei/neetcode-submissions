class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val:index
        found = {}
        for i in range (len(nums)):
            val = nums[i]
            remains = target - val
            idx = found.get(remains)
            if idx is not None:
                return [idx, i]
            found[val] = i
        return []