class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        if x == 0:
            return float(0)

        negative = n < 0
        exponent = abs(n)

        def recursion(x: float, n: int) -> float:
            if n == 1:
                return x
            
            if n == 2:
                return x*x

            if n % 2 == 0:
                res = recursion(x, n//2)
                return res*res
            
            res = recursion(x, n//2)
            return res*res*x

        res = recursion(x, exponent)
        return 1/res if negative else res