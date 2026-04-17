class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 有向图，找最短，边有权重，只有正权重
        
        # bellman-ford 算法
        start = k
        INF = 2**31-1
        # [0]空缺，INF代表还没求出距离
        min_time = [INF] * (n+1)
        min_time[start] = 0

        # 这种解法下，可以不需要邻接表或邻接矩阵，只用边列表
        # 优点：稀疏图中效率高，也不需要额外空间
        # 缺点：每次都要遍历所有边，即使不再更新距离的边

        # 循环 n-1 轮，n是节点数
        # 循环次数的依据是：最短路径最多包含n-1条边，所以需要n-1轮来保证信息传递到最远节点
        # 可以提前终止的条件是，在任意轮如果所有边都没有更新，说明已经找到最短路径了
        for _ in range(n-1):
            updated = False
            # 遍历所有的边
            for time in times:
                from_n, to_n, weight = time[0], time[1], time[2]
                # 根据距离表，如果dist[n] 还是 INF 占位符，就代表：
                # 1.从 start 起点没有到 n 节点的路径
                # 2.可能有路径，目前还没遍历到，但是后面的轮次会更新
                # 在python中不会溢出，但为了严格表达这个语义，就加上此判断
                if (min_time[from_n] != INF and 
                    min_time[from_n]+weight < min_time[to_n]):
                    min_time[to_n] = min_time[from_n]+weight
                    updated = True

            if not updated:
                break

        # 额外的一轮检查是处理负环
        # 有的图会有负权重的边，继续更新会不断变小
        # 节点：
        # 0, 1, 2
        # 边及权重：
        # 0→1 : 1
        # 1→2 : 1
        # 2→0 : -3
        # for time in times:
        #     from_n, to_n, weight = time[0], time[1], time[2]
        #     if min_time[from_n]+weight<min_time[to_n]:
        #         return -1

        total_time = 0
        for i in range(1, len(min_time)):
            if min_time[i] == INF:
                return -1
            total_time = max(total_time, min_time[i])
        return total_time