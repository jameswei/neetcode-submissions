class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # start[i]无重复
        # 安排meetingroom以小的room编号优先 0<k1<k2<n，k1优先
        # delayed meeting以原有的早的start优先，start[i]<start[j]，[i]优先
        # 这道题和meeting room II 不同的是，对于重叠冲突的会议，不扩展room，而是按顺序延期
        # 有空room了，就从小编号的room开始排

        # meeting room举行会议的数量
        room_held_meeting_count = [0] * n

        # (start,end)
        available_meetings = []
        for m in meetings:
            heapq.heappush(available_meetings, (m[0], m[1]))

        # (结束时间,房间编号)
        available_rooms = []
        for k in range(n):
            heapq.heappush(available_rooms, (-1, k))

        
        # 最早会议起始时间
        cur_time = available_meetings[0][0]

        while len(available_meetings) > 0:
            # 直到没有meeting需要安排
            while len(available_meetings) > 0 and available_meetings[0][0] >= cur_time:
                (meeting_start, meeting_end) = heapq.heappop(available_meetings)
                
                if available_rooms[0][0] == -1 or meeting_start >= available_rooms[0][0]:
                    (_, room_num) = heapq.heappop(available_rooms)
                    heapq.heappush(available_rooms, (meeting_end, room_num))
                    room_held_meeting_count[room_num] += 1
                
                else:
                    # 延迟meeting
                    heapq.heappush(available_meetings, (available_rooms[0][0], meeting_end+available_rooms[0][0]-meeting_start))

            cur_time = available_rooms[0][0]

        max_count = 0
        min_room_num = 0
        for i in range(n):
            if room_held_meeting_count[i] > max_count:
                max_count = room_held_meeting_count[i]
                min_room_num = i

        return min_room_num
            