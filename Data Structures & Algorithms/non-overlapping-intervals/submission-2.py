class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        print(f"intervals: {intervals}")
        min_removal = 0
        i, n = 1, len(intervals)
        prev_end = intervals[0][1]

        while i < n:
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            # overlapped
            if cur_start < prev_end:
                min_removal += 1
                prev_end = min(prev_end, cur_end)
            else:
                prev_end = cur_end

            i += 1
            
        return min_removal
            