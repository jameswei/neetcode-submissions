class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 单个堆的解法
        # (end_time, room_id)
        # 初始状态每个room都空闲，所以end_time为0
        rooms = [(0, x) for x in range(n)]
        heapq.heapify(rooms)

        meetings.sort(key=lambda x: (x[0], x[1]))

        count = [0] * n

        for i in range(len(meetings)):
            start_time, end_time = meetings[i][0], meetings[i][1]

            # 找到所有空闲的room，end_time早于当前meeting的start_time
            # 为了满足分配room时的规则——始终选择编号小的可用room
            # 将所有空闲的room的第一排序key（也就是end_time）设置成一样（当前meeting的start_time），这样就能利用上第二排序key（room_id）
            while len(rooms) > 0 and rooms[0][0] < start_time:
                # 找待选room的条件也可以用 rooms[0][0] <= start_time，只不过白出堆入堆一趟
                (_, room_id) = heapq.heappop(rooms)
                heapq.heappush(rooms, (start_time, room_id))

            # 从空闲room中选出room编号最小的
            last_end_time, room_id = heapq.heappop(rooms)
            # 安排上
            new_end_time = last_end_time + end_time - start_time
            # 更新空闲时间
            heapq.heappush(rooms, (new_end_time, room_id))
            # 计数
            count[room_id] += 1

        return count.index(max(count))