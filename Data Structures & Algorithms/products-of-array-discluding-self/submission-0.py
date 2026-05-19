class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self = [1] * len(nums)
        total_product = 1
        has_zero = False
        for num in nums:
            if num == 0:
                has_zero = True
                continue;
            total_product *= num
        for i in range(len(nums)):
            if has_zero:
                if nums[i] != 0:
                    product_except_self[i] = 0
                else:
                    product_except_self[i] = total_product    
            else:
                product_except_self[i] = total_product // nums[i]

        return product_except_self