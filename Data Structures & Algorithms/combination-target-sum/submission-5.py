class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = list()

        def dfs(target: int, i: int, selection: List[int]):
            if target == 0:
                res.append(selection.copy())
                return

            # no available options
            if i >= len(nums):
                return
            
            # prune uncessary selections
            if nums[i] > target:
                return
            
            # select nums[i]
            selection.append(nums[i])
            dfs(target-nums[i], i, selection)
            selection.pop()

            # or not
            dfs(target, i+1, selection)
        
        dfs(target, 0, [])
        
        return res