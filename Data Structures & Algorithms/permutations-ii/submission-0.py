class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 排列问题，重复元素算作一种排列，所以递归时相同元素要跳过就都要跳过
        # 排序是保持单调性，相同元素聚集在一起
        nums.sort()
        n = len(nums)

        res = []

        def dfs(used: set[int], path):
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(n):
                if i in used:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in used:
                    continue

                used.add(i)
                path.append(nums[i])
                dfs(used, path)
                used.remove(i)
                path.pop()
            
        dfs(set(), [])
        return res