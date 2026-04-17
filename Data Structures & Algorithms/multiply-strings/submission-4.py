class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1_digit = [int(x) for x in num1[::-1]]
        num2_digit = [int(x) for x in num2[::-1]]

        m, n = len(num1), len(num2)
        product_digit = [0] * (m+n)

        for i in range(m):
            digit_1 = num1_digit[i]

            carry = 0
            for j in range(n):
                digit_2 = num2_digit[j]

                val = digit_1 * digit_2 + product_digit[i+j] + carry
                product_digit[i+j] = val % 10
                carry = val // 10

            if carry > 0:
                product_digit[i+n] = carry

        k = 0
        while product_digit[::-1][k] == 0:
            k += 1

        return ''.join([str(x) for x in product_digit[::-1][k:]])
        