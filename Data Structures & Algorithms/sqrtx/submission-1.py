class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        i, j = 0, x

        while i <= j:
            mid = i+(j-i)//2
            sqr = mid**2

            if sqr == x:
                return mid
            elif sqr < x:
                i = mid + 1
            else:
                j = mid -1

        return j