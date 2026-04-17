class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1

        # +2147483647
        max_val = 2**31-1
        # -2147483648
        min_val = -(2**31)

        rev = 0
        num = abs(x)
        while num > 0:
            r = num % 10
            num = num // 10
            # 不需要，如果当前取得的最低位一直是0，
            # 那么rev=0*10+0 依然是0
            # if r == 0:
            #     continue
            
            rev = rev * 10 + r
            if sign*rev < min_val or sign*rev > max_val:
                return 0
            
            # 检查溢出

        return sign * rev