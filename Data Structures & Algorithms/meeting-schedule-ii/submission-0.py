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

        meetings = intervals
        days = 0

        while len(meetings) > 0:
            meetings.sort(key=lambda time: time.end)
            prev_end = meetings[0].end

            overlapped = list()

            for i in range(1, len(meetings)):
                cur_start = meetings[i].start

                if cur_start< prev_end:
                    overlapped.append(meetings[i])
                else:
                    prev_end = intervals[i].end

            meetings = overlapped

            days += 1

        return days