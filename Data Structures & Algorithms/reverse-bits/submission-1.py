class Solution:
    def reverseBits(self, n: int) -> int:
        # 0001 0101
        # 1010 1000

        res = 0b0

        for i in range(32):
            lowest_bit = (n >> i) & 0b1
            res += lowest_bit << (31 - i)
        return res