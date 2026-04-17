class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # [left, right]范围内所有数字的bit and操作
        # 可以观察出，由于and操作的规则是给定bit位都为1得1，剩下情况都为0
        # 最终结果中，对于给定bit位，只有在原范围内的所有数的这个bit位都为1，才能得1，否则就是0
        # 如果对于所有数依次检查每个bit位，依然很慢
        # 但是给定范围内的连续整数，它们在二进制形式上只是某些bit位发生变化
        # 一旦某一位在某个数里变成0，那最终结果的这一位也是0
        # 所以只需要从高位到低位，检查从哪一位开始“不同”
        # 从这一位开始往后（也就是直到最低位），在最终结果里都是0
        # 因为在这个位范围内，必然是0、1交替的情况，and操作后只能是0
        # 而最终结果就只有高位相同的部分后面用0补齐
        # 从left到right的连续整数，正是代表从left和right的高位相同部分之后，每一位都在经历0、1循环
        # 所以问题转化成，找到left和right的二进制公共前缀

        shift = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            shift += 1

        return left << shift