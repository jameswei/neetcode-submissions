class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        for _ in range(k):
            nums[i-k], nums[i] = nums[i], nums[i-k]
            i -= 1
        
        return