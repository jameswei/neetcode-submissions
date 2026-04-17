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

        
        # 收到的节点所需时间，默认无穷，[0]空缺
        received_time = [2**31-1] * (n+1)

        # 优先级队列，以某条路径到该节点的时间
        queue = [(0, start)]

        # bfs 遍历
        def bfs():
            while len(queue) > 0:
                # 每次只选择耗时最小的节点
                elapsed, from_node = heapq.heappop(queue)

                # 如果以当前路径到达此节点的时间多于以前的路径，直接放弃这条路径
                if elapsed > received_time[from_node]:
                    continue

                # 更短时间到达此节点，那就更新到达时间表
                received_time[from_node] = elapsed

                # 如果有可达节点
                to_nodes = adj_list[from_node]
                if len(to_nodes) > 0:
                    for (time, to_node) in to_nodes:
                        heapq.heappush(queue, (elapsed+time, to_node))

        bfs()
        
        total_time = 0
        for i in range(1, n+1):
            # 要求全部节点都被覆盖
            if received_time[i] == 2**31-1:
                return -1
            
            total_time = max(total_time, received_time[i])
        
        return total_time