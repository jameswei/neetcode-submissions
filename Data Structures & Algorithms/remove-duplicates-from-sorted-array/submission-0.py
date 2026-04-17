class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        distinct_nums = []

        prev = 2**31-1

        for num in nums:
            if num != prev:
                distinct_nums.append(num)
            prev = num
        
        k = len(distinct_nums)
        for i in range(k):
            nums[i] = distinct_nums[i]
        
        return k