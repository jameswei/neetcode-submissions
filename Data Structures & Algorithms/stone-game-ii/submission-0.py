class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[None] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        def dfs(i: int, M: int) -> int:
            if i == n:
                return 0
            if dp[i][M] is not None:
                return dp[i][M]

            res = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                res = max(res, suffix_sum[i] - dfs(i + X, max(M, X)))
            dp[i][M] = res
            return res

        return dfs(0, 1)