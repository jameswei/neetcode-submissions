class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # (l,r)左开右开区间，因为0和n+1位置都放了dummy
        new_nums = [1] + nums + [1]
        memo = [[-1] * (n+2) for _ in range(n+2)]

        def dfs(l: int, r: int) -> int:
            if l + 1 == r:
                return 0

            if memo[l][r] != -1:
                return memo[l][r]

            coins = 0
            for k in range(l+1, r):
                coins = max(coins, dfs(l, k) + new_nums[l]*new_nums[k]*new_nums[r] + dfs(k, r))
            
            memo[l][r] = coins
            return coins

        return dfs(0, n+1)