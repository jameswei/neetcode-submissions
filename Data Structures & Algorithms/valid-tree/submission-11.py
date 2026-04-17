class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        # adjacent list
        # [i]->[]
        graph = [[] for _ in range(n)]

        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(i: int, last: int) -> bool:
            if i in visited:
                return False

            visited.add(i)

            if len(graph[i]) == 0:
                return True
            
            for e in graph[i]:
                if e == last:
                    continue
                if not dfs(e, i):
                    return False
            
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n