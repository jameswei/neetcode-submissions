"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda time: time.end)

        prev_end = intervals[0].end
        i, n = 1, len(intervals)

        while i < n:
            cur_start = intervals[i].start
            cur_end = intervals[i].end

            if cur_start < prev_end:
                return False
            
            prev_end = cur_end
            i += 1

        return True
