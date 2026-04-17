class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree nodes must be fully connected, n nodes must have n-1 edges
        print(f"total edges: {len(edges)}, total nodes: {n}")
        if len(edges) != n-1:
            return False

        # graph[i][j] edge between i and j
        graph = [[0] * n for _ in range(n)]

        for edge in edges:
            if edge[0] == edge[1]:
                # failed at here?
                continue
            a, b = edge[0], edge[1]
            graph[a][b], graph[b][a] = 1, 1

        # n=5
        # edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
        # | 0 1 0 0 0 |
        # | 1 0 1 1 1 |
        # | 0 1 0 1 0 |
        # | 0 1 1 0 0 |
        # | 0 1 0 0 0 |

        
        def dfs(i: int, visited: set[int], nodes: list[int]) -> bool:
            if i in visited and i != nodes[-1]:
                return False
            
            visited.add(i)
            nodes.append(i)

            for j in range(len(graph[i])):
                if graph[i][j] == 0:
                    continue
                
                dfs(j, visited, nodes)
                
            return True
        
        visited = set()
        connected_nodes = list()
        if not dfs(0, visited, connected_nodes):
            return False
        
        return len(connected_nodes) == n