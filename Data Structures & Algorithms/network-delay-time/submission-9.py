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
        received_time[start] = 0

        # 优先级队列，以某条路径到该节点的时间
        queue = [(0, start)]

        # bfs 遍历
        def bfs():
            while len(queue) > 0:
                # 每次只选择耗时最小的节点
                elapsed, from_node = heapq.heappop(queue)

                # 如果以当前路径到达此节点的时间多于以前的路径，直接放弃这条路径
                # 即便是入队前有检查，此处也依然需要！
                # 出队列后的检查称为“严格检查”，目的是确认该路径是否确实是“最佳的”，或是已经“没意义”了
                # 允许<= 的路径，说明这就是“松弛检查”筛选来的路径，应该继续处理
                # 使用>= 也可以，是一种更严格的确保每个节点只处理一次
                if elapsed >= received_time[from_node]:
                    continue

                # 如果有可达节点
                to_nodes = adj_list[from_node]
                for (time, to_node) in to_nodes:
                    # 如果以此路径到达下一节点的时间已经多于其他路径曾经到达的时间，直接放弃此路径
                    # 入队前的检查称作“松弛检查”，目的是只允许“新的、有可能成为最佳/短路径的节点入队列”
                    # 这也是为什么使用< 而不是 <= 的原因，相等的情况下说明曾经已经有等长的路径了，没必要重复探索
                    if elapsed+time < received_time[to_node]:
                        received_time[to_node] = elapsed+time
                        heapq.heappush(queue, (elapsed+time, to_node))

        bfs()
        
        total_time = 0
        for i in range(1, n+1):
            # 要求全部节点都被覆盖
            if received_time[i] == 2**31-1:
                return -1
            
            total_time = max(total_time, received_time[i])
        
        return total_time