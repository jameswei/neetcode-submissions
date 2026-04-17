class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # unique integers!
        # 要所有的组合，不需要排序

        res = []

        def dfs(i: int, path: list[int]):
            if i > len(nums)-1:
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            dfs(i+1, path)

        dfs(0, [])

        return res
        