class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_with_first = nums[0:len(nums)-1]
        max_amount_with_first = [0] * len(nums_with_first)
        max_amount_with_first[0] = nums_with_first[0]
        max_amount_with_first[1] = max(nums_with_first[1], nums_with_first[0])
        for i in range(2, len(nums_with_first)):
            max_amount_with_first[i] = max(nums_with_first[i]+max_amount_with_first[i-2], max_amount_with_first[i-1])

        nums_without_first = nums[1:]
        max_amount_without_first = [0] * len(nums_without_first)
        max_amount_without_first[0] = nums_without_first[0]
        max_amount_without_first[1] = max(nums_without_first[1], nums_without_first[0])
        for i in range(2, len(nums_without_first)):
            max_amount_without_first[i] = max(nums_without_first[i]+max_amount_without_first[i-2], max_amount_without_first[i-1])

        return max(max_amount_with_first[len(nums_with_first)-1], max_amount_without_first[len(nums_without_first)-1])


