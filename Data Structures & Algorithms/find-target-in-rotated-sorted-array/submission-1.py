class Solution:
    def binary_search(self, nums: List[int], l, r, target: int) -> int:
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        target_idx = -1
        l, r = 0, len(nums) - 1

        m = l + (r - l) // 2
        if nums[m] == target:
            target_idx = m
        if nums[m] > nums[r]:
            if nums[l] <= target and target < nums[m]:
                # go to left
                target_idx= self.binary_search(nums, l, m - 1, target)
            else:
                target_idx = self.binary_search(nums, m + 1, r , target)
        elif nums[m] < nums[r]:
            if nums[m] < target and target <= nums[r]:
                # go to right
                target_idx = self.binary_search(nums, m + 1, r, target)
            else:
                target_idx = self.binary_search(nums, l, m - 1, target)

        return target_idx
