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

        def dfs(i: int, total: int, path: list[int]):
            if len(path) == 4:
                if total == target:
                    res.append(path[:])
                return

            # 剪枝，剩余数不够凑出四元组
            if n - i < 4 - len(path):
                return

            # 因为单调递增，还可以通过“剩余和”和剩余可选中的“最大和”或“最小和”比较
            remaining_nums = 4-len(path)
            remaining = target-total
            if sum(nums[i:i+remaining_nums]) > remaining:
                return
            if sum(nums[-remaining_nums:]) < remaining:
                return

            for j in range(i, n):
                if nums[j] > 0 and total+nums[j] > target:
                    break

                # 这个保证了相同数不会重复选择
                if j > i and nums[j] == nums[j-1]:
                    continue

                # 选
                path.append(nums[j])
                dfs(j+1, total+nums[j], path)
                # 撤销选择后就等同于不选，进入下一轮循环
                path.pop()
                # 不选，后续相同数都不选，
                
            
        dfs(0, 0, [])
        return res