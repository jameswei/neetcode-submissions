class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        if self.rank[parent_x] > self.rank[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_x] = parent_y
            self.rank[parent_y] += 1

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 从图得到最小生成树，满足全连接、无环，同时边权重和最小
        # 顶点最多100个，边最多200
        # 之后再找关键边和伪关键边
        # 是否关键的含义是如果图中不包含该边，则会使得所有最小生成树的权重和都变大；
        # 隐含条件是该边存在于所有的最小生成树中（由于移除，导致新的生成树的权重和变大）
        # 伪关键边表达同样的性质，但不是出现于所有的最小生成树中

        """
        排序：将所有边按权重从小到大排序。
        贪心选择：从小到大遍历每条边。
        判断环：用Union-Find检查当前边的两个端点是否已经连通（即是否属于同一个集合）。
        如果未连通，则选中这条边（它不会形成环），用Union操作合并两端点，并将权重加入总和。
        如果已连通，则跳过这条边（加入它会形成环）。
        终止条件：当选中了 n-1 条边时，已经形成了一棵生成树，算法可以提前结束。或者遍历完所有边后，检查选中的边是否达到 n-1 条来判断图是否连通。
        """

        def kruskal_mst(include_idx: int = -1, exclude_idx: int = -1) -> int:
            # kruskal要依赖union-find动态生成连通量
            union_find = UnionFind(n)

            connected_count = 0
            weight_sum = 0

            if include_idx != -1:
                for (u, v, w, i) in edge_with_idx:
                    if i == include_idx:
                        if union_find.union(u, v):
                            weight_sum += w
                            connected_count += 1
                        break

            for (u,v,w,i) in edge_with_idx:
                if i == include_idx or i == exclude_idx:
                    continue
                
                if union_find.union(u, v):
                    weight_sum += w
                    connected_count += 1
                    # mst全连通，要求n-1条边
                    if connected_count == n-1:
                        break

            return weight_sum if connected_count == n-1 else 2**31-1

        edge_with_idx = [(u, v, w, i) for i, (u,v,w) in enumerate(edges)]
        edge_with_idx.sort(key=lambda x: x[2])

        mst_weight_sum = kruskal_mst()

        # 根本无法构成mst
        if mst_weight_sum == 2**31-1:
            return []
        
        critical_edges = []
        pseudo_critical_edges = []

        for (_,_,_,i) in edge_with_idx:
            weight_sum_without_edge = kruskal_mst(exclude_idx=i)
            # 只要去掉该边，mst权重会增加，那一定是关键边（因为要存在于所有mst中）
            if weight_sum_without_edge > mst_weight_sum:
                critical_edges.append(i)
                continue
            
            # 如果不是关键边，那再判断是否伪关键边
            else:
                weight_sum_pre_conn_edge = kruskal_mst(include_idx=i)
                if weight_sum_pre_conn_edge == mst_weight_sum:
                    pseudo_critical_edges.append(i)
            
        return [critical_edges, pseudo_critical_edges]