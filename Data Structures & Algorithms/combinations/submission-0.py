class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 组合问题
        if k == n:
            return [[x+1 for x in range(n)]]

        nums = [x+1 for x in range(n)]

        res = []
        def dfs(i: int, comb: list[int]):
            if len(comb) == k:
                res.append(comb[:])
                return

            if i == n:
                return
            
            comb.append(nums[i])
            dfs(i+1, comb)
            comb.pop()

            dfs(i+1, comb)

        dfs(0, [])
        return res
