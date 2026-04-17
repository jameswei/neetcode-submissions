class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid)-1, len(grid[0])-1

        islands = []
        max_area = 0

        def dfs(x: int, y: int, island: list[tuple[int,int]]):
            if x < 0 or x > m:
                return

            if y < 0 or y > n:
                return

            if grid[x][y] == 0:
                return

            island.append((x,y))

            #原地修改避免重复访问
            grid[x][y] = 0

            dfs(x-1, y, island)
            dfs(x+1, y, island)
            dfs(x, y-1, island)
            dfs(x, y+1, island)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue

                island = []
                dfs(i, j, island)
                islands.append(island)
                max_area = max(max_area, len(island))

        return max_area
        