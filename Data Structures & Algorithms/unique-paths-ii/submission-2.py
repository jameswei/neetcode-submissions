class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dirs = [(0, 1), (1, 0)]
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i == m-1 and j == n-1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]
            
            count = 0
            for d_i, d_j in dirs:
                n_i, n_j = i+d_i, j+d_j
                if 0 <= n_i <= m-1 and 0 <= n_j <= n-1 and obstacleGrid[n_i][n_j] == 0:
                    count += dfs(n_i, n_j)

            memo[(i, j)] = count
            return count

        return dfs(0, 0)