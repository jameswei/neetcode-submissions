class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 本质是数学中的最大公因数，这里是变成两个字符串的最大公因部分（也就是gcd通过重复，能够组成str1和str2）
        a, b = max(len(str1), len(str2)), min(len(str1), len(str2))
        # 两个参与者比较的不是数值，而且组成部分，所以根据二者长度直接使用“欧几里得算法”
        # gcd(a,b) = gcd(b,a % b)

        if str1 not in str2 and str2 not in str1:
            return ""

        if str1+str2 != str2+str1:
            return ""

        while a % b > 0:
            r = a % b
            a = b
            b = r

        return str2[0:b] if len(str1) > len(str2) else str1[0:b]
