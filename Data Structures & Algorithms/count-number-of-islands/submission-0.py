class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        groups = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]:                        
                    self.dfs(grid, visited, i, j)
                    groups += 1
                visited[i][j] = True

        return groups

    def dfs(self, grid: List[List[str]], visited: List[List[bool]], row: int, col: int):
        if row < 0 or row > len(grid)-1:
            return
        if col < 0 or col > len(grid[row])-1:
            return

        if visited[row][col]:
            return

        print(f"[{row}][{col}]: {grid[row][col]}")
        visited[row][col] = True
        
        if grid[row][col] == "0":
            return

        self.dfs(grid, visited, row, col-1)
        self.dfs(grid, visited, row, col+1)
        self.dfs(grid, visited, row-1, col)
        self.dfs(grid, visited, row+1, col)