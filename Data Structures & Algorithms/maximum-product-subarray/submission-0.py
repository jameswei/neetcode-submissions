class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = 1
        max_product_matrix = [1] * len(nums)

        max_product_matrix[0] = nums[0]
        max_product = max(max_product, max_product_matrix[0])

        for i in range (1, len(nums)):
            max_product_matrix[i] = max(nums[i], nums[i]*max_product_matrix[i-1])
            max_product = max(max_product, max_product_matrix[i])

        return max_product
