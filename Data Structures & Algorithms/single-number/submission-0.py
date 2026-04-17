class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 利用xor 特性，a xor a == 0
        val = 0b0
        for n in nums:
            val = val ^ n
        return val