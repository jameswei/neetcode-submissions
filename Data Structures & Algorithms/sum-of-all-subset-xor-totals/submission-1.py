class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo = {}

        def dfs(i: int, xor_sum: int) -> int:
            if i == n:
                return xor_sum

            val = nums[i]

            # 选择或不选择
            return dfs(i+1, xor_sum^val) + dfs(i+1, xor_sum)

        return dfs(0, 0)
