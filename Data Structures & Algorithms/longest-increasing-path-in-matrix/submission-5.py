class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 从记忆化 dfs 解法也可以改成 dp 解法
        memo = [[-1] * n for _ in range(m)]

        longest_path = 0

        def dfs(i: int, j: int) -> int:
            if memo[i][j] != -1:
                return memo[i][j]

            max_len = 0
            for (d_i, d_j) in dirs:
                n_i, n_j = i+d_i, j+d_j
                if (0 <= n_i < m and 0 <= n_j < n and 
                    matrix[n_i][n_j] > matrix[i][j]):
                    max_len = max(max_len, dfs(n_i, n_j))

            memo[i][j] = max_len + 1

            return memo[i][j]

        for i in range(m):
            for j in range(n):
                if memo[i][j] == -1:
                    longest_path = max(longest_path, dfs(i, j))

        return longest_path