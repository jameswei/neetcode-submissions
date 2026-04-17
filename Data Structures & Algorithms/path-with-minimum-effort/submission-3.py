class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        # 问题是找出具有最小的最大落差的路径
        # 把落差看成边的权重，题目就转化成最短路径问题
        # Dijkstra算法是适合的解法(bfs+priority queue)，总是沿着权重最小的路径探索
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # (diff, row, col)
        min_effort_neighbor = [(0, 0, 0)]
        INF = 2**31-1
        min_effort_to = [[INF] * n for _ in range(m)]
        min_effort_to[0][0] = 0

        while len(min_effort_neighbor) > 0:

            min_effort, row, col = heapq.heappop(min_effort_neighbor)

            if min_effort > min_effort_to[row][col]:
                continue

            if row == m - 1 and col == n - 1:
                return min_effort

            for d_row, d_col in dirs:
                n_row, n_col = row+d_row, col+d_col

                if 0 <= n_row < m and 0 <= n_col < n:
                    n_effort = max(min_effort, abs(heights[row][col]-heights[n_row][n_col]))
                    if n_effort < min_effort_to[n_row][n_col]:
                        min_effort_to[n_row][n_col] = n_effort
                        heapq.heappush(min_effort_neighbor, (n_effort, n_row, n_col))
        
        return 0