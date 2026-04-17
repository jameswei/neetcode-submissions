"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1

        meetings, max_meeting_rooms = 0, 0

        time_slot = list()

        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            time_slot.append((start, 1))
            time_slot.append((end, -1))

        time_slot.sort(key=lambda x: (x[0], x[1]))

        for i in range(len(time_slot)):
            meetings += time_slot[i][1]
            max_meeting_rooms = max(max_meeting_rooms, meetings)
        
        return max_meeting_rooms