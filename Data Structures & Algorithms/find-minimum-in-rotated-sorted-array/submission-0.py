class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right]:
                # go to left
                right = mid - 1
            else:
                # go to right
                left = mid
        return nums[left]