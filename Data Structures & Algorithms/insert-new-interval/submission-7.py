class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        n_itv = newInterval
        res = list()
        i, n = 0, len(intervals)

        while i<n and intervals[i][1]<n_itv[0]:
            res.append(intervals[i])
            i += 1

        while i<n and intervals[i][0]<=n_itv[1]:
            n_itv[0] = min(intervals[i][0], n_itv[0])
            n_itv[1] = max(intervals[i][1], n_itv[1])
            i += 1
        res.append(n_itv)
        
        while i<n:
            res.append(intervals[i])
            i += 1
        
        return res