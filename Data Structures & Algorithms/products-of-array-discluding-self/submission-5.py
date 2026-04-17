class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix_product = 1
        for i in range(0, len(nums)):
            result[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= suffix_product
            suffix_product *= nums[j]

        return result