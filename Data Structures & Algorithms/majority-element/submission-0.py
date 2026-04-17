class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n, maj = len(nums), len(nums)//2

        prev = nums[0]
        count = 1
        for i in range(1, n):
            if nums[i] == prev:
                count += 1
            else:
                prev = nums[i]
                count = 1
            
            if count > maj:
                return prev

        return prev
