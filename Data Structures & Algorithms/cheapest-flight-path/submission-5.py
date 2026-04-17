class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 朴素想法
        # 沿用bfs+dijkstra解法，只不过搜索过程会提前终止，
        # 因为只需要在有限条件下（不超过k 次中间节点），找到目标节点。

        start, end = src, dst
        max_stops = k
        # 邻接表，from_n:[(price, to_n)...]
        adj_list = [[] for _ in range(n)]

        for flight in flights:
            from_n, to_n, price = flight[0], flight[1], flight[2]
            adj_list[from_n].append((price, to_n))

        INF = 2**31-1
        # cheapest_to[i][j] 停留j次到达i站的最低成本，j范围是[0, max_stop+1]
        # 但是除起点外cheapest_to[*][0] 无意义，因为其他节点 stops 最少1次
        cheapest_to = [[INF] * (max_stops+2) for _ in range(n)]
        # price 优先级队列，起点的stop数是0，
        # 这里stops的含义是落地次数，从起点直飞的任意节点stops是1，落地一次了
        # 考虑到给定最多停留次数k，指的是起点和终点之间的最大次数，那么终点的stops是[1,max_stops+1]范围
        queue = [(0, start, 0)]

        while len(queue) > 0:
            (price, airport, stops) = heapq.heappop(queue)
            # stops 靠入队前检查
            
            # 飞到目的地了
            if airport == end:
                # 记录以该路径停留stops次到达目的地的成本
                cheapest_to[end][stops] = min(cheapest_to[end][stops], price)

            # 其他路径以相同停留数到达此节点时成本更低，这条路径直接放弃
            if price > cheapest_to[airport][stops]:
                continue

            # 从该节点往其他节点飞
            for (next_price, next_airport) in adj_list[airport]:
                # 比其他路径以相同停留数到达下个节点成本更低，值得探索
                if (stops < max_stops+1 and 
                    price+next_price < cheapest_to[next_airport][stops+1]):
                    heapq.heappush(queue, (price+next_price, next_airport, stops+1))
                    cheapest_to[next_airport][stops+1] = price+next_price

        cheapest_price = INF
        for stop in range(1, max_stops+2):
            cheapest_price = min(cheapest_to[end][stop], cheapest_price)

        return -1 if cheapest_price == INF else cheapest_price