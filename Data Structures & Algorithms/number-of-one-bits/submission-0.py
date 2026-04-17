class Solution:
    def hammingWeight(self, n: int) -> int:
        flag = 0b1

        count = 0
        for i in range(32):
            mask = flag << i
            if mask == mask & n:
                count += 1

        return count