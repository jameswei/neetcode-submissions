class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0)]
        INF = 2**31-1
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i == m-1 and j == n-1:
                return grid[i][j]

            if (i, j) in memo:
                return grid[i][j] + memo[(i, j)]

            min_sum = INF
            for d_i, d_j in dirs:
                n_i, n_j = i+d_i, j+d_j
                if 0 <= n_i <= m-1 and 0 <= n_j <= n-1:
                    min_sum = min(min_sum, dfs(n_i, n_j))

            memo[(i, j)] = grid[i][j] + min_sum
            return grid[i][j] + min_sum

        return dfs(0, 0)