class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_amount_with_first = [0] * len(nums)
        max_amount_with_first[0] = nums[0]
        max_amount_with_first[1] = 0
        for i in range(2, len(nums)-1):
            max_amount_with_first[i] = max(nums[i]+max_amount_with_first[i-2], max_amount_with_first[i-1])
        max_amount_with_first[len(nums)-1]= max_amount_with_first[len(nums)-2]

        max_amount_without_first = [0] * len(nums)
        max_amount_without_first[0] = 0
        max_amount_without_first[1] = nums[1]
        for i in range(2, len(nums)):
            max_amount_without_first[i] = max(nums[i]+max_amount_without_first[i-2], max_amount_without_first[i-1])

        return max(max_amount_with_first[len(nums)-1], max_amount_without_first[len(nums)-1])


