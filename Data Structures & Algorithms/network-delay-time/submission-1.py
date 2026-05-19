class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 有向图
        # times[i] = [ui, vi, ti]

        # 找最短，边有权重
        # 层序遍历+priority queue

        # 建邻接表，用数组会有空位，代表该节点无可达节点
        # 稀疏情况下会有浪费，所以也可以用dict
        # [0]空缺
        adj_list = [[] for _ in range(n+1)]

        for edge in times:
            from_n, to_n, time = edge[0], edge[1], edge[2]

            adj_list[from_n].append((time, to_n))

        # 建堆，每个from_node一个基于时间的优先级队列
        for node in range(1, n+1):
            heapq.heapify(adj_list[node])

        print(f"adj_list: {adj_list}, start: {k}")

        # 起点
        start = k
        # 收到的节点
        received_nodes = set([start])

        queue = deque([start])
        total_time = 0

        # bfs 遍历
        def bfs():
            nonlocal total_time

            while len(queue) > 0:
                nodes_in_cur_level = len(queue)
                
                for _ in range(nodes_in_cur_level):
                    from_node = queue.popleft()
                    to_nodes = adj_list[from_node]
                    # 如果有可达节点
                    if len(to_nodes) > 0:
                        # 按照时间代价选择可达节点
                        (time, to_node) = heapq.heappop(to_nodes)
                        # 同时要避免已经到过的节点
                        if to_node not in received_nodes:
                            queue.append(to_node)
                            received_nodes.add(to_node)
                
                if len(queue) > 0:
                    total_time += 1

        bfs()
        # 要求全部节点都被覆盖
        return total_time if len(received_nodes) == n else -1