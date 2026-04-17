class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 开始从起点到终点，乘客上车下车，这是一个天然的线性的过程
        # 所以旅程以pickup的位置由近至远先后发生
        trips.sort(key=lambda t: t[1])

        # 乘客的增减只发生在两个情况下，旅程开始增，旅程结束减
        # 始终确保乘客数不超过承载量，否则就失败

        # 用堆来维护进行中的旅程，记录旅程的终点位置和乘客数量 (drop_off_pos, passengers)
        ongoing_trips = []
        
        # 当前乘客数量
        cur_passengers = 0

        for trip in trips:
            passengers, pick_up_pos, drop_off_pos = trip

            # 有旅程已经结束了
            while len(ongoing_trips) > 0 and ongoing_trips[0][0] <= pick_up_pos:
                _, prev_passengers = heapq.heappop(ongoing_trips)
                # 减去下车的乘客
                cur_passengers -= prev_passengers
                
            # 加上本次旅程的乘客
            cur_passengers += passengers
            # 如果超过承载量
            if cur_passengers > capacity:
                return False

            # 加入进行中的行程
            heapq.heappush(ongoing_trips, (drop_off_pos, passengers))

        return True

