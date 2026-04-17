class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        # num_of_one_int_bits(val // 2 == val >> 1) + 1 if val & 0b1 == 1 else 0
        dp = [0] * (n+1)

        for i in range(1, n+1):
            print(f"nums: {i}, binary: {format(i, '08b')}, >>1: {i>>1}, count: {dp[i>>1]}, i&1: {i&0b1}")
            dp[i] = dp[i>>1] + (i & 0b1)

        return dp
