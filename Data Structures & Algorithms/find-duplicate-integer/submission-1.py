class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # len(nums) = n+1, nums[i] 在 [1,n]区间
        for i in range(len(nums)):
            num = nums[i]
            idx = num - 1

            if nums[idx] == 0:
                return num
            
            nums[idx] = 0

        return 0

        