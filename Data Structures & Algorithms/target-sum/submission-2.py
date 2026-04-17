class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = {}

        def dfs(i: int, total: int) -> int:
            if total == target and i > n-1:
                return 1

            if i > n-1:
                return 0

            if (i, target-total) in memo:
                return memo[(i, target-total)]
            
            val = nums[i]

            ans = 0
            # 两种情况
            ans += dfs(i+1, total+(1*val)) + dfs(i+1, total+(-1*val))

            memo[(i, target-total)] = ans
            return ans
        
        total = dfs(0, 0)

        return total