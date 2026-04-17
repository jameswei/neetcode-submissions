class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2**31 - 1

        def bfs(x: int, y: int, visited: set[tuple[int, int]]) -> int:
            queue = deque()
            queue.append((x, y))
            distance = 0

            while len(queue) > 0:

                for _ in range(len(queue)):
                    (i, j) = queue.popleft()

                    if i < 0 or i > m-1 or j < 0 or j > n-1:
                        continue
                    if (i, j) in visited:
                        continue
                    if grid[i][j] == -1:
                        continue

                    visited.add((i, j))

                    if grid[i][j] == 0:
                        return distance

                    queue.append((i, j-1))
                    queue.append((i, j+1))
                    queue.append((i-1, j))
                    queue.append((i+1, j))

                distance += 1

            return INF

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j, set())

        return