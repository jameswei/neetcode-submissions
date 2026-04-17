class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2**31 - 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 多源 bfs，同时从多个终点找起点
        def bfs(treasure_pos: list[tuple[int, int]], visited: set[tuple[int, int]]):
            queue = deque(treasure_pos)
            distance = 0

            while len(queue) > 0:

                for _ in range(len(queue)):
                    (i, j) = queue.popleft()

                    if grid[i][j] == INF:
                        grid[i][j] = distance

                    for di, dj in dirs:
                        ni, nj = i+di, j+dj
                        if (ni, nj) not in visited and 0<=ni<=m-1 and 0<=nj<=n-1 and grid[ni][nj] != -1:
                            queue.append((ni, nj))
                            visited.add((ni, nj))

                distance += 1

            return
        
        treasure_pos = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasure_pos.append((i, j))

        bfs(treasure_pos, set())

        return