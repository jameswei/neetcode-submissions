class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 完全图上的最小生成树的问题：
        # 全连接（n-1个边），无环，成本最低
        # Kruskal算法：贪心地从小到大加边，只要不形成环就加入，是否成环依靠union-find/disjoint-set union
        
        # 全连接的边及权重
        edges = {}
        # 总是考虑权重最小的边
        min_heap = []
        # 并查集
        parents = {}

        def find(u) -> tuple[int, int]:
            if parents[u] != u:
                parents[u] = find(parents[u])

            return parents[u]

        def union(u, v):
            parents[find(u)] = find(v)

        for i in range(len(points)):
            x_i, y_i = points[i]
            parents[i] = i

            for j in range(i+1, len(points)):
                x_j, y_j = points[j]
                
                # 曼哈顿距离
                cost = abs(x_i-x_j) + abs(y_i-y_j)

                edges[(i, j)] = cost
                heapq.heappush(min_heap, (cost, (i, j)))

        print(f"edges: {edges}, parents: {parents}")

        min_cost = 0    
        while len(min_heap) > 0:
            # 当前最小代价的边
            (cost, (i, j)) = heapq.heappop(min_heap)
            # 检查 DSU
            p_i = find(i)
            p_j = find(j)
            if p_i != p_j:
                min_cost += cost
                union(i, j)
        
        return min_cost