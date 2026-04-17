class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 这个解法不同时移位left和right，而是只移位right，直到它小于等于left

        while left < right:
            right = right & (right-1)

        return right