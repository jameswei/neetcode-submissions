class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2**31-1
        treasure = 0
        water = -1

        m = len(grid)
        n = len(grid[0])

        def dfs(x: int, y: int, visited: set[tuple[int, int]]) -> int:
            if x < 0 or x > m-1:
                return land

            if y < 0 or y > n-1:
                return land
            
            if grid[x][y] == water:
                return land

            if grid[x][y] == treasure:
                return treasure
                
            if (x, y) in visited:
                return grid[x][y]

            visited.add((x, y))
            
            distance = min(dfs(x, y-1, visited), 
                        dfs(x, y+1, visited), 
                        dfs(x-1, y, visited), 
                        dfs(x+1, y, visited))
            
            visited.remove((x, y))
            
            return 1+distance if distance != land else land


        for i in range(m):
            for j in range(n):
                if grid[i][j] == land:
                    grid[i][j] = dfs(i, j, set())

        return