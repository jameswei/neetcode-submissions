class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 排列问题，重复元素算作一种排列，所以递归时相同元素要跳过就都要跳过
        # 排序式得相同元素聚集在一起
        nums.sort()
        n = len(nums)
        used = set()
        res = []

        def dfs(path):
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
                dfs(path)
                used.remove(i)
                path.pop()
            
        dfs([])
        return res