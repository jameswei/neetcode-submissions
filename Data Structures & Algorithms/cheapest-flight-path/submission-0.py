class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 朴素想法
        # 沿用bfs+dijkstra解法，只不过搜索过程会提前终止，
        # 因为只需要在有限条件下（不超过k 次中间节点），找到目标节点。

        start, end = src, dst
        max_stops = k
        # 邻接表，from_n:[(price, to_n)...]
        adj_list = [[] for _ in range(len(flights))]

        for flight in flights:
            from_n, to_n, price = flight[0], flight[1], flight[2]
            adj_list[from_n].append((price, to_n))

        print(f"adj_list: {adj_list}")

        # price 优先级队列
        queue = [(0, start, 0)]
        INF = 2**31-1
        total_price = INF 

        while len(queue) > 0:
            (price, airport, stops) = heapq.heappop(queue)

            if airport == end and stops <= max_stops+1:
                # 更新价钱，退出
                total_price = min(total_price, price)

            if price > total_price:
                continue

            for (next_price, next_airport) in adj_list[airport]:
                # 价钱划得来，且中转不超过要求
                if (price+next_price) < total_price and stops <= max_stops:
                    heapq.heappush(queue, (price+next_price, next_airport, stops+1))

        return -1 if total_price == INF else total_price