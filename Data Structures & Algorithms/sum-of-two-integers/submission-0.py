class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0

        mask = 0b1
        carry = 0b0

        # [0,31]
        for i in range(32):
            lowest_bit_of_a = a & mask
            lowest_bit_of_b = b & mask

            sum_of_bit = lowest_bit_of_a ^ lowest_bit_of_b ^ carry

            if lowest_bit_of_a == 0b1 and lowest_bit_of_b == 0b1:
                carry = 0b1
            else:
                carry = 0b0
            
            res ^= sum_of_bit << i

            a >>= 1
            b >>= 1
        
        return res