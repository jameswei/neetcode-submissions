class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        negative = x < 0
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

            # 计算前先检查溢出
            # 这里目的是在python之外的语言，比如c 语言中，先计算就会真的产生溢出错误
            # 所以计算前，把计算过程分成两部分来检查：
            # rev*10前，把 rev 和 max_val//10比
            # +r前，把 r 和 max_val%10比
            if rev > max_val//10:
                return 0
            if rev == max_val//10 and r > max_val%10:
                return 0
            
            rev = rev * 10 + r

        return sign * rev if min_val <= sign*rev <= max_val else 0