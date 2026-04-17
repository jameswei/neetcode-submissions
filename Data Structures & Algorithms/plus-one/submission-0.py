class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)-1

        total = 0
        for i in range(len(digits)):
            d = digits[i]
            total += d * 10**(n-i)

        num = total + 1
        print(f"total: {total}, total+1: {num}")

        res = []
        while num > 0:
            res.append(num % 10)
            num = num // 10
        
        return res[::-1]

