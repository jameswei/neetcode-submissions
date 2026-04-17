class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0

        def dfs(grid: List[List[str]], row: int, col: int):
            if row < 0 or row > len(grid)-1:
                return
            if col < 0 or col > len(grid[row])-1:
                return
            
            if grid[row][col] == "0":
                return

            grid[row][col] = '0'

            dfs(grid, row, col-1)
            dfs(grid, row, col+1)
            dfs(grid, row-1, col)
            dfs(grid, row+1, col)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands += 1

        return islands