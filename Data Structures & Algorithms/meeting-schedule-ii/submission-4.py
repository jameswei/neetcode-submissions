"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort meeting by start time
        intervals.sort(key=lambda meeting: meeting.start)
        
        # a min heap holds in-progress meetings
        in_progress_meetings = []

        for meeting in intervals:
            if len(in_progress_meetings) > 0 and in_progress_meetings[0] <= meeting.start:
                heapq.heappop(in_progress_meetings)

            heapq.heappush(in_progress_meetings, meeting.end)

        return len(in_progress_meetings)
        