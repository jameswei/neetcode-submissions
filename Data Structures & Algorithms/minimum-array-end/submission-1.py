class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # 生成一组数，个数为n，单调递增，并且所有数的and操作等于x，返回最后一个数
        # 所有数的按位and操作要求==x，就要求每个数都必须包含x中所有为1的位，否则那一位and操作后会变成0
        # 但是对于x中为0的位则只要不是所有数的这一位都是1即可，只要有一个0，and操作就变成0

        # The key insight is that the answer must have all bits of x set, 
        # and we need to "count" to n - 1 using only the bit positions where x has 0s.
        res = x
        i_x = 1
        i_n = 1  # for n-1

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res = res | i_x
                i_n = i_n << 1
            i_x = i_x << 1

        return res