class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        target_idx = -1
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                target_idx = m
                break
            if nums[m] > nums[r]:
                # go to right
                l = m + 1
            else:
                # go to left
                r = m - 1

        return target_idx
        