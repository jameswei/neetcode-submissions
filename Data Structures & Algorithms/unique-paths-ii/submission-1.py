class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 起点是(0,0)，终点是(m-1,n-1)
        # 终点可以从上方或左方移动过来，按这个方式递推
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == n == 1 and obstacleGrid[0][0] == 1:
            return 0
        
        # [i][j]作为起点可以到达终点的路径数
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        dirs = [(0, 1), (1, 0)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    for d_i, d_j in dirs:
                        n_i, n_j = i+d_i, j+d_j
                        if 0 <= n_i <= m-1 and 0 <= n_j <= n-1 and obstacleGrid[n_i][n_j] == 0:
                            dp[i][j] += dp[n_i][n_j]

        return dp[0][0]
        