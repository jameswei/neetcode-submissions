class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        shortest_length = defaultdict(lambda: -1)

        sorted_queries = queries[:]
        sorted_queries.sort()

        # 以 left_i 单调增
        intervals.sort(key=lambda x : x[0])
        
        # 小顶堆，(length, end)
        min_heap = []
        
        i = 0

        for j in range(len(sorted_queries)):
            query = sorted_queries[j]
            
            while i<len(intervals) and intervals[i][0] <= query:
                heapq.heappush(min_heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1

            # interval[j] starts after query

            while len(min_heap) > 0 and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # either heap is empty or 
            # the top element covers query also has the shortest length
            if len(min_heap) > 0:
                shortest_length[query] = min_heap[0][0]
            
        res = []
        for k in queries:
            res.append(shortest_length[k])
        
        return res