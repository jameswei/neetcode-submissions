class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        # 先排序,获得单调递增
        nums.sort()
        if nums[0] > target:
            return []
        
        # 朴素 dfs
        res = []
        # 这个解法会因为nums中包含相同的数字，从而产生重复解
        # 改进方式是将res改成set，放入quadruple
        def dfs(i: int, total: int, path: list[int]):
            if total == target and len(path) == 4:
                res.append(path[:])
                return

            if i > n-1 or len(path) > 4:
                return

            for j in range(i, n):
                if total+nums[j] > target:
                    return
                if j > i and nums[j] == nums[j-1]:
                    continue

                # 选
                path.append(nums[j])
                dfs(j+1, total+nums[j], path)
                path.pop()
                
                # 不选，后续相同数都不选，靠上面nums[j] == nums[j-1] continue来保证
            
        dfs(0, 0, [])
        return res