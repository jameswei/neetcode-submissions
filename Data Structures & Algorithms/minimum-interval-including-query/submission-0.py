class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for i in range(len(queries)):
            query = queries[i]

            shortest_length = -1
            for j in range(len(intervals)):
                interval = intervals[j]
                if query < interval[0] or query > interval[1]:
                    continue
                
                if shortest_length == -1:
                    shortest_length = interval[1]-interval[0]+1
                else:
                    shortest_length = min(shortest_length, (interval[1]-interval[0]+1))
            
            res.append(shortest_length)
        
        return res