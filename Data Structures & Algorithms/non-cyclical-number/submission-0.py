class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        seen = set()
        total = 0
        
        while total != 1 and total not in seen:
            
            while n > 0:
                total += (n%10) ** 2
                n = n // 10
            
            seen.add(total)

        return total == 1