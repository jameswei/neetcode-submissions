class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # len(nums) = n+1, nums[i] 在 [1,n]区间
        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num - 1

            # already marked
            if nums[idx] < 0:
                return num
            
            nums[idx] = nums[idx] * -1

        return 0

        