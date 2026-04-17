class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree nodes must be fully connected, n nodes must have n-1 edges
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

        
        def dfs(i: int, nodes: list[int]) -> bool:
            if i in nodes and i != nodes[-1]:
                return False
            
            nodes.append(i)

            for j in range(len(graph[i])):
                if graph[i][j] == 0:
                    continue
                
                dfs(j, nodes)
                
            return True
        
        connected_nodes = list()
        if not dfs(0, connected_nodes):
            return False
        
        return len(connected_nodes) == n