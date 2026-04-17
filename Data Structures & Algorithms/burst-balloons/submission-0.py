class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 本质上是“顺序依赖”的决策问题：当前做的每个选择，都会改变剩余问题的结构

        n = len(nums)
        new_nums = [1] + nums + [1]
        
        # (l,r)左开右开区间，因为0和n+1位置都放了dummy

        def dfs(l: int, r: int) -> int:
            if l + 1 == r:
                return 0

            coins = 0
            for k in range(l+1, r):
                coins = max(coins, dfs(l, k) + new_nums[l]*new_nums[k]*new_nums[r] + dfs(k, r))
            
            return coins


        return dfs(0, n+1)