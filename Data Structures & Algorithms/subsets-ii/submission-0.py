class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 把重复的数排在一起
        nums.sort()

        res = []

        def dfs(i: int, path: list[int]):
            if i > len(nums)-1:
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            while i+1<len(nums) and nums[i+1]==nums[i]:
                i += 1
            dfs(i+1, path)

        dfs(0, [])

        return res