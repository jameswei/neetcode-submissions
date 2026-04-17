class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid)-1, len(grid[0])-1

        max_area = 0

        # 由于只求最大面积，可以不记录island对应的格子
        # 递归函数就只需要传坐标
        def dfs(x: int, y: int) -> int:
            if x < 0 or x > m:
                return 0

            if y < 0 or y > n:
                return 0

            if grid[x][y] == 0:
                return 0

            #原地修改避免重复访问
            grid[x][y] = 0

            return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue

                area = dfs(i, j)
                max_area = max(max_area, area)

        return max_area
