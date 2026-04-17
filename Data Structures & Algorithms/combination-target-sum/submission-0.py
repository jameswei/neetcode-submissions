class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 可重复组合，核心思想：
        # 做选择
        # 递归
        # 取消选择

        # 排序保证单调增
        nums.sort()

        self.res = []
        
        def dfs(nums: List[int], start: int, remains: int, selection: List[int]):
            if remains < 0:
                # no answer in this path
                return
            elif remains == 0:
                # found an answer
                self.res.append(selection.copy())
                return
            
            for i in range(start, len(nums)):
                num = nums[i]

                # select nums[i]
                remains -= num
                selection.append(num)

                dfs(nums, i, remains, selection)
                
                # restore
                remains += num
                selection.pop()

                # or not select nums[i]
                # dfs(nums, i+1, remains, selection)
                # no need to explicitly skip, after restoring the state
                # and in next loop, i++ means skipped
                
                

        dfs(nums, 0, target, list())

        return self.res