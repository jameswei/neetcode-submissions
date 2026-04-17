class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 记忆化 dfs
        memo = [[-1] * n for _ in range(m)]

        longest_path = 0

        def dfs(i: int, j: int, last_val: int) -> int:
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return 0
            
            val = matrix[i][j]
            if val <= last_val:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            max_len = 0
            for (d_i, d_j) in dirs:
                n_i, n_j = i+d_i, j+d_j
                max_len = max(max_len, dfs(n_i, n_j, val))

            memo[i][j] = max_len + 1

            nonlocal longest_path
            longest_path = max(longest_path, memo[i][j])

            return memo[i][j]

        for i in range(m):
            for j in range(n):
                if memo[i][j] == -1:
                    dfs(i, j, memo[i][j])

        return longest_path