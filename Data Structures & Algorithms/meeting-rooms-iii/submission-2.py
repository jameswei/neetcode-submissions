class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 单个堆的解法
        # (end_time, room_num)
        # 初始状态每个room都空闲，所以end_time为0
        rooms = [(0, x) for x in range(n)]
        heapq.heapify(rooms)

        meetings.sort(key=lambda x: (x[0], x[1]))

        count = [0] * n

        for i in range(len(meetings)):
            start_time, end_time = meetings[i][0], meetings[i][1]

            while len(rooms) > 0 and rooms[0][0] < start_time:
                (_, room_num) = heapq.heappop(rooms)
                heapq.heappush(rooms, (start_time, room_num))

            room = heapq.heappop(rooms)
            new_end_time = room[0] + end_time - start_time
            heapq.heappush(rooms, (new_end_time, room[1]))
            count[room[1]] += 1

        return count.index(max(count))