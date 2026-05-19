class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 0 1 0 0 0
        # 0 0 1 1 1
        # 0 0 0 1 0
        # 0 0 0 0 0
        # false

        # 0 1 1 1 0
        # 0 0 0 0 1
        # 0 0 0 0 0
        # 0 0 0 0 0
        # true

        node_graph = [[0] * n for _ in range(n)]

        for edge in edges:
            node_graph[edge[0]][edge[1]] = 1

        def dfs(row: int, col: int) -> bool:
            if row+1 <= len(node_graph)-1:
                if node_graph[row+1][col] == 1:
                    return False
                if not dfs(row+1, col):
                    return False
            return True

        
        for i in range(len(node_graph)):
            for j in range(len(node_graph[i])):
                if node_graph[i][j] == 0:
                    continue
                if not dfs(i, j):
                    return False
                
        return True