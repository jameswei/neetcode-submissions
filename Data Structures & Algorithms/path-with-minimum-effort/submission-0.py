class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        min_effort = 2**31-1
        def dfs(i: int, j: int, cur_max_diff: int, visited: set[tuple[int, int]]):
            nonlocal min_effort
            if i == m - 1 and j == n - 1:
                # 到终点
                min_effort = min(min_effort, cur_max_diff)
                return

            for d_i, d_j in dirs:
                n_i, n_j = i+d_i, j+d_j

                if 0 <= n_i <= m-1 and 0 <= n_j <= n-1 and (n_i, n_j) not in visited:
                    visited.add((n_i, n_j))
                    dfs(n_i, n_j, max(cur_max_diff, abs(heights[i][j]-heights[n_i][n_j])), visited)
                    visited.remove((n_i, n_j))
                
            return

        dfs(0, 0, 0, set([(0,0)]))
        return min_effort

