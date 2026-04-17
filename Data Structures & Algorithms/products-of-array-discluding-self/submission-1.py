class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self = [1] * len(nums)
        total_product_without_zero = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            total_product_without_zero *= num
        for i in range(len(nums)):
            if zero_count == 0:
                product_except_self[i] = total_product_without_zero // nums[i]
            elif zero_count > 1:
                product_except_self[i] = 0
            elif zero_count == 1 and nums[i] != 0:
                product_except_self[i] = 0
            else:
                product_except_self[i] = total_product_without_zero

        return product_except_self