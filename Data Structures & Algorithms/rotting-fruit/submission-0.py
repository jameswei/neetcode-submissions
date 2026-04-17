class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(rotten_fruits: list[tuple[int, int]], fresh_fruits_count: int) -> int:
            lvl_count = 0
            queue = deque(rotten_fruits)

            while len(queue) > 0:
                for _ in range(len(queue)):
                    (i, j) = queue.popleft()
                    
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1:
                            queue.append((ni, nj))
                            grid[ni][nj] = 2
                            fresh_fruits_count -= 1
                    
                lvl_count += 1

            return lvl_count-1 if fresh_fruits_count == 0 else -1

        rotten_fruits = []
        total_fresh_fruits = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_fresh_fruits += 1
                elif grid[i][j] == 2:
                    rotten_fruits.append((i, j))
        
        if total_fresh_fruits == 0:
            return 0

        return bfs(rotten_fruits, total_fresh_fruits)
