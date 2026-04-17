class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        start, end = (0, 0), (n-1, n-1)
        INF = 2**31-1
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        queue = [(grid[start[0]][start[1]], start)]
        # 状态表，表示[i][j]达到 grid[i][j]的最短耗时
        time_to = [[INF] * n for _ in range(n)]
        # 初始化起点
        time_to[0][0] = grid[start[0]][start[1]]

        min_time = INF

        while len(queue) > 0:
            
            (time, (i, j)) = heapq.heappop(queue)

            # if time > time_to[i][j]:
            #     continue

            # 到终点了，一定是最短的
            if (i, j) == end:
                return time
                
            for (d_i, d_j) in dirs:
                n_i, n_j = i+d_i, j+d_j
                # 入队检查
                # 先检查越界与否，再检查状态表，看看此路径是否值得
                if 0<=n_i<n and 0<=n_j<n:
                    n_elevation = grid[n_i][n_j]
                    n_time = max(time, n_elevation)
                    if n_time < time_to[n_i][n_j]:
                        # 更新状态表
                        time_to[n_i][n_j] = n_time

                        heapq.heappush(queue, (n_time, (n_i, n_j)))


                
        return min_time