class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 接着就从记忆化+dfs 解法改成 dp 解法

        n = len(nums)
        memo = [[-1] * n for _ in range(n)]

        # [l,r]
        def dfs(l: int, r: int) -> int:
            if r < 0 or l > n-1 or l > r:
                return 0

            if memo[l][r] != -1:
                return memo[l][r]

            max_coins = 0

            # 在[l,r]中选择k作为最后戳破的气球
            for k in range(l, r+1):
                # 这是错误的！因为这个逻辑表达的含义是“先戳破[k]气球”，
                # 如果是这样的话，那它的原左不变，原右部分就会向左移动，剩余数组长度-1，结构发生了变化！
                # 而这里递归的思路是把[k]当作最后戳破的气球。
                # coins = (1 if k-1 < 0 else nums[k-1])*nums[k]*(1 if k+1>n-1 else nums[k+1])
                coins = (nums[l-1] if l-1 >= 0 else 1)*nums[k]*(nums[r+1] if r+1 < n else 1)
                coins += dfs(l, k-1)
                coins += dfs(k+1, r)

                max_coins = max(max_coins, coins)
            
            memo[l][r] = max_coins
            return max_coins
        
        return dfs(0, n-1)