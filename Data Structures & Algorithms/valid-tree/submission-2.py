class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # only one node
        if n == 1:
            return True
        # no edges means no connectivity
        if len(edges) == 0:
            return False

        # graph[i][j] edge between i and j
        graph = [[0] * n for _ in range(n)]

        for edge in edges:
            a, b = edge[0], edge[1]

            graph[a][b], graph[b][a] = 1, 1

        # n=5
        # edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
        # | 0 1 0 0 0 |
        # | 1 0 1 1 1 |
        # | 0 1 0 1 0 |
        # | 0 1 1 0 0 |
        # | 0 1 0 0 0 |

        
        def dfs(i: int, visited: set[int]) -> bool:
            if i in visited:
                return False
            
            visited.add(i)

            if i+1 < len(graph[i]):
                for j in range(i+1, len(graph[i])):
                    if graph[i][j] == 0:
                        continue
                    
                    if not dfs(j, visited):
                        return False
                
            return True
        
        visited = set()
        if not dfs(0, visited):
            return False
        
        return len(visited) == n