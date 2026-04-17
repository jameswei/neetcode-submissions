class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        # 稀疏图用邻接表
        graph = [[] * _ for _ in range(n)]

        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            # undirected graph
            graph[v].append(u)

        def dfs(i: int, last: int, group: set[int]):
            if i in group or i == last:
                return
            
            group.add(i)

            neighbors = graph[i]
            if len(neighbors) == 0:
                return

            for j in neighbors:
                if j == last:
                    continue
                dfs(j, i, group)

            return

        nodes = set()
        num_of_group = 0
        for i in range(n):
            if i not in nodes:
                dfs(i, -1, nodes)
                num_of_group += 1

        return num_of_group
            