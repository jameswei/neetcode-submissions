class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 朴素思路
        # bfs从起点到终点，检查已消耗时间是否>=终点的elevation
        # 是，则取消耗时间；否，则取终点elevation
        # 防止走回头路需要加visited
        # 但实际还会有重复的探索，所以需要状态来表示
        # 从[x,y]能到终点的最少时间

        # bfs选择下个节点时，需要满足条件：
        # 能过去，消耗时间>=elevation
        # 疑问：
        # 1.是否还需要优先级队列？
        # 2.在任意位置，如果没有可选下个节点怎么办？
        # 我理解依然需要优先级队列，以elevation作为优先级
        # 入队列时按照候选点加入
        # 出队前检查对头elevation和已消耗时间，如果不够，继续等待

        n = len(grid)
        start, end = (0, 0), (n-1, n-1)
        INF = 2**31-1
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        queue = [(grid[start[0]][start[1]], start)]
        # 状态表，表示[i][j]达到 grid[i][j]目前最短耗时
        time_to = [[INF] * n for _ in range(n)]

        min_time = INF
        elapsed = 0

        while len(queue) > 0:
            
            (elevation, (i, j)) = heapq.heappop(queue)
            elapsed = max(elevation, elapsed)

            if elapsed > time_to[i][j]:
                continue
            
            # 更新状态表
            time_to[i][j] = elapsed

            if (i, j) == end:
                min_time = min(min_time, elapsed)
                break
                
            else:
                for (d_i, d_j) in dirs:
                    n_i, n_j = i+d_i, j+d_j
                    # 入队检查
                    # 先检查越界与否，再检查状态表，看看此路径是否值得
                    if 0<=n_i<n and 0<=n_j<n:
                        n_elevation = grid[n_i][n_j]
                        if max(elapsed, n_elevation) < time_to[n_i][n_j]:
                            heapq.heappush(queue, (n_elevation, (n_i, n_j)))


                
        return min_time