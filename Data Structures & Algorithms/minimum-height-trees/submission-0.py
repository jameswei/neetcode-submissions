class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 树是特殊的图，全连接、无向、无环
        # 找出所有最小高度的树（的根）
        # 等同于图里找最短路径，bfs
        # 任意节点都可以做根，所以对所有节点bfs

        if n == 1:
            return [n-1]
        
        # 根据edges建邻接表
        adj_table = defaultdict(set)
        for edge in edges:
            node_1, node_2 = edge[0], edge[1]
            adj_table[node_1].add(node_2)
            adj_table[node_2].add(node_1)

        def bfs(queue: deque, visited: set[int]):
            height = 0

            while len(queue) > 0:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    # 根据邻接表找neighbor
                    for next_node in adj_table[node]:
                        if next_node not in visited:
                            queue.append(next_node)
                            visited.add(next_node)

                if len(queue) > 0:
                    height += 1

            return height

        # {height:[node]}
        res = defaultdict(list)

        for i in range(n):
            height_from_i = bfs(deque([i]), set([i]))
            print(f"height from {i}: {height_from_i}")
            res[height_from_i].append(i)

        return res[min(res.keys())]