class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        self.res = list()

        def dfs(nums: List[int], target: int, start: int, selection: List[int]):
            if target == 0:
                self.res.append(selection.copy())
            
            for i in range(start, len(nums)):
                num = nums[i]

                if num > target:
                    break
                
                selection.append(num)
                
                dfs(nums, target-num, i, selection)

                selection.pop()

        dfs(nums, target, 0, list())

        return self.res