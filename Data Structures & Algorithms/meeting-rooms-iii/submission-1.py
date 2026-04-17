class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 只关注关键的时间点：会议的开始时刻和结束时刻
        meetings.sort(key=lambda x : (x[0], x[1]))

        # (end_time, room_num)按最早空闲时间建堆
        unavailable_rooms = []
        
        # 按room编号排序
        available_rooms = [x for x in range(n)]
        heapq.heapify(available_rooms)

        room_meeting_count = [0] * n

        for i in range(len(meetings)):
            start_time, end_time = meetings[i][0], meetings[i][1]

            while len(unavailable_rooms) > 0 and unavailable_rooms[0][0] <= start_time:
                _, room_num = heapq.heappop(unavailable_rooms)
                heapq.heappush(available_rooms, room_num)

            if len(available_rooms) > 0:
                room_num = heapq.heappop(available_rooms)
                heapq.heappush(unavailable_rooms, (end_time, room_num))
                room_meeting_count[room_num] += 1
            
            else:
                (last_end_time, room_num) = heapq.heappop(unavailable_rooms)
                heapq.heappush(unavailable_rooms, (last_end_time+(end_time-start_time), room_num))
                room_meeting_count[room_num] += 1
            

        max_count = 0
        min_room_num = 0
        for i in range(len(room_meeting_count)):
            if room_meeting_count[i] > max_count:
                max_count = room_meeting_count[i]
                min_room_num = i

        return min_room_num

