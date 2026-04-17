class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        used_num = [False] * len(nums)
        res = []

        def dfs(path: list[int]):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                n = nums[i]
                
                if used_num[i]:
                    continue
                
                path.append(n)
                used_num[i] = True

                dfs(path)

                path.pop()
                used_num[i] = False

        dfs([])
        return res