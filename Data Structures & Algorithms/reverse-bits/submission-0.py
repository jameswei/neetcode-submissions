class Solution:
    def reverseBits(self, n: int) -> int:
        # 0001 0101
        # 1010 1000

        res = 0b0

        for i in range(32):
            if (n >> i) & 0b1 == 0b1:
                res += 0b1 << (31-i)
            else:
                continue

        return res