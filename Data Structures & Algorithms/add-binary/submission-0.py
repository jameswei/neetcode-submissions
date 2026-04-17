class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)

        if len_a < len_b:
            a = "0" * (len_b-len_a) + a
        elif len_a > len_b:
            b = '0'*(len_a-len_b) + b

        print(f"a: {a}, b: {b}")
        n = len(a)
        carry = 0
        res = ""
        for i in range(n-1, -1, -1):
            num_a, num_b = int(a[i]), int(b[i])
            i_sum = num_a+num_b+carry

            carry = i_sum // 2
            res += str(i_sum % 2)
        
        if carry > 0:
            res += str(carry)

        return res[::-1]

            
        