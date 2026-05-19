class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 有向图
        # times[i] = [ui, vi, ti]
        # 找最短，边有权重
        # 层序遍历+priority queue

        # 起点
        start = k
        # 建邻接表，[0]空缺，用数组会有空位，代表该节点无可达节点
        # 稀疏情况下会有浪费，所以也可以用dict
        adj_list = [[] for _ in range(n+1)]
        for edge in times:
            from_n, to_n, time = edge[0], edge[1], edge[2]

            adj_list[from_n].append((time, to_n))

        # 建堆，每个from_node一个基于时间的优先级队列
        for node in range(1, n+1):
            heapq.heapify(adj_list[node])

        # 收到的节点所需时间，默认无穷，[0]空缺
        received_time = [2**31-1] * (n+1)
        # 起点不需要时间
        received_time[start] = 0

        # 队列，以某条路径到该节点的时间
        queue = deque([(0, start)])

        # bfs 遍历
        def bfs():
            while len(queue) > 0:
                nodes_in_cur_level = len(queue)
                
                for _ in range(nodes_in_cur_level):
                    elapsed, from_node = queue.popleft()
                    to_nodes = adj_list[from_node]

                    # 如果有可达节点
                    if len(to_nodes) > 0:
                        while len(to_nodes) > 0:
                            (time, to_node) = heapq.heappop(to_nodes)
                            if to_node != start:
                                if elapsed+time <= received_time[to_node]:
                                    # 更新到达时间表
                                    received_time[to_node] = elapsed+time
                                    queue.append((elapsed+time, to_node))

        bfs()

        total_time = 0
        # 要求全部节点都被覆盖
        for i in range(1, n+1):
            if received_time[i] == 2**31-1:
                return -1
            else:
                total_time = max(total_time, received_time[i])
        
        return total_time