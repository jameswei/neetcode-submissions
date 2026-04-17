class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 本质是有向图的欧拉路径
        # tickets 描述的飞行路径，所有的 city 就是节点，飞行路径就是两个节点的有向边
        # 固定以 JFK 作为起点
        # 要求每条路线都要走一次，所以可能会形成环
        # 这种情况下“拓扑排序”也就是 Khan 算法就不适用了，因为它只适合 DAG，有向无环图
        
        # 如果每个节点的入度==出度，说明有“欧拉回路”，可以通过遍历tickets来构建节点入度表
        # 构建出入度表后，从起点开始 DFS 探索
        # 选择节点时的第一优先级是字典序（lexicography order）
        
        airport_in = defaultdict(int)
        airport_out = defaultdict(int)
        destinations_from = defaultdict(list)

        for ticket in tickets:
            from_airport, to_airport = ticket[0], ticket[1]
            airport_in[to_airport] += 1
            airport_out[from_airport] += 1

            heapq.heappush(destinations_from[from_airport], to_airport)
        
        # 建完入度表、出度表后，如果入度==出度，都算是候选起点
        start_airport = "JFK"
        airports_in_path = []

        def dfs(airport: str, path: list[str]):
            if len(destinations_from[airport]) == 0:
                return

            while len(destinations_from[airport]) > 0:
                next_airport = heapq.heappop(destinations_from[airport])
                dfs(next_airport, path)
                path.append(next_airport)


            return

        flight_path = []
        dfs(start_airport, flight_path)

        return [start_airport] + flight_path[::-1]