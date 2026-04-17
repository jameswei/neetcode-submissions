class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # perimeter就是求周长
        m, n = len(grid), len(grid[0])
        # 周长取决于整个island中每个cell的接壤情况，每个cell有4条边，每有一个接壤的cell，周长-1
        # 所以应该记录island中每个cell的接壤数量，换个角度就是记录每个cell应该被计入周长的边数

        edge_count = [[0] * n for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(i: int, j: int):
            # (i,j) 只会被访问一次，根据它4个方向是否接壤来记录边数
            edge = 4

            for d_i, d_j in dirs:
                n_i, n_j = i+d_i, j+d_j
                
                # 如果4个方向有接壤的cell
                if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] == 1:

                    edge -= 1

                    if (n_i, n_j) not in visited:
                        visited.add((n_i, n_j))
                        dfs(n_i, n_j)
            
            edge_count[i][j] = edge

            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
        

        total_edges = 0
        for i in range(m):
            for j in range(n):
                if edge_count[i][j] > 0:
                    total_edges += edge_count[i][j]

        return total_edges * 1
