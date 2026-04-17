class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        intervals.sort()
        print(f"intervals: {intervals}")

        i, j, n = 0, 1, len(intervals)
        min_removal = 0

        while i < n:
            # move j util found overlapped interval
            while j<n and intervals[i][1]<=intervals[j][0]:
                i = j
                j +=1
            
            if j == n:
                break

            len_i = intervals[i][1]-intervals[i][0]
            len_j = intervals[j][1]-intervals[j][0]

            print(f"found overlapped, {intervals[i]}:{len_i} - {intervals[j]}:{len_j}")
            
            min_removal += 1

            if len_i>len_j and intervals[i][1]>=intervals[j][1]:
                i = j
            
            j += 1
            
        return min_removal
            