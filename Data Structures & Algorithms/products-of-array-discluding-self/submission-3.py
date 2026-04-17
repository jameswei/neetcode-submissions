class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self = [0] * len(nums)
        total_product_without_zero = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
                # more than 1 zero
                if zero_count > 1:
                    return product_except_self
            else:
                total_product_without_zero *= num
        
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    product_except_self[i] = total_product_without_zero
        else:
            # zero_count == 0
            for i in range(len(nums)):
                product_except_self[i] = total_product_without_zero // nums[i]

        return product_except_self