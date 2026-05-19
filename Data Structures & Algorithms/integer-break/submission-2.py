class Solution:
    def integerBreak(self, n: int) -> int:
        # k在[2,n]范围，尝试n可以被k整除的情况下，求商q的k次方。在所有结果中找出最大值

        max_product = 1
        k = 2
        while k <= n:
            if n % k == 0:
                quotient = n // k
                max_product = max(max_product, quotient**k)
            
            k += 1
        
        return max_product