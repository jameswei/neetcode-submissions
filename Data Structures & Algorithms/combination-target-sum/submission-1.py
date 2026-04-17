class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序保证单调增
        nums.sort()

        self.res = []
        
        def dfs(nums: List[int], start: int, remains: int, selection: List[int]):
            if remains == 0:
                # found an answer
                self.res.append(selection.copy())
                return
            
            for i in range(start, len(nums)):
                num = nums[i]

                # prune unnecessary selections
                # no answer in this pasth
                if num > remains:
                    return

                # select nums[i]
                remains -= num
                selection.append(num)

                dfs(nums, i, remains, selection)
                
                # restore
                remains += num
                selection.pop()

                # or not select nums[i]
                # dfs(nums, i+1, remains, selection)
                # there's no need to explicitly skip, after restoring the state
                # and in next loop, i++ means skipped
                
        dfs(nums, 0, target, list())

        return self.res