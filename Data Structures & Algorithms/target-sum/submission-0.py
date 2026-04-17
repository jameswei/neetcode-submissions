class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 全排列？
        # 也不算，是保持原有顺序的情况下，每个位置做选择？
        n = len(nums)
        res = []
        def dfs(i: int, total: int, path: list[int]):
            if total == target and len(path) == n:
                res.append(path[:])
                return

            if i > n-1:
                return
            
            val = nums[i]

            # 两种情况
            path.append(1*val)
            dfs(i+1, total+(1*val), path)
            path.pop()

            path.append(-1*val)
            dfs(i+1, total+(-1*val), path)
            path.pop()
        
        dfs(0, 0, [])

        return len(res)