class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # [left, right]范围内所有数字的bit and操作
        res = left

        for i in range(left, right+1):
            res = res & i

        return res