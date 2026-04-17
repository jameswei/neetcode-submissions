class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            suffix_product[j] = suffix_product[j+1] * nums[j+1]

        result = []
        for i in range(len(nums)):
            result.append(prefix_product[i] * suffix_product[i])
        
        return result