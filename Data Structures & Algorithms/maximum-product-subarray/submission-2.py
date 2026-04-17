class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_product = 0
        max_product_matrix = [1] * len(nums)
        max_product_matrix[0] = nums[0]
        max_product = max(max_product, max_product_matrix[0])

        min_product = 0
        min_product_matrix = [1] * len(nums)
        min_product_matrix[0] = nums[0]


        for i in range (1, len(nums)):
            temp_max = nums[i] * max_product_matrix[i-1]
            temp_min = nums[i] * min_product_matrix[i-1]

            max_product_matrix[i] = max(nums[i], temp_max, temp_min)
            max_product = max(max_product, max_product_matrix[i])

            min_product_matrix[i] = min(nums[i], temp_min, temp_max)
            

        return max_product
