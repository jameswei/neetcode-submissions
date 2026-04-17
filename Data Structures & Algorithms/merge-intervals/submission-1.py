class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()

        res = list()

        i, j, n = 0, 0, len(intervals)

        while i < n:
            start, end = intervals[i][0], intervals[i][1]
            while j<n and start<=intervals[j][0]<=end:
                end = max(end, intervals[j][1])
                j += 1

            res.append([start, end])

            i = j
        
        return res