class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        # subset不要求连续，但要求相对顺序，包含重复元素的子集是不同的子集，包括空集和全集
        def dfs(i: int, path: list[int]) -> int:
            if i == n:
                xor_sum = 0
                for num in path:
                    xor_sum = xor_sum ^ num

                return xor_sum

            val = nums[i]
            total_sum = 0
            # 选择或不选择
            path.append(val)
            total_sum += dfs(i+1, path)
            path.pop()

            total_sum += dfs(i+1, path)

            return total_sum

        total_sum = 0
        total_sum += dfs(0, [])
        return total_sum
