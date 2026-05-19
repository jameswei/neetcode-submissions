class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = list()
        
        # intervals=[[1,2],[3,5],[9,10]]
        # newInterval=[6,7]

        # intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
        # newInterval=[4,8]

        look_back = False
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if look_back:
                if start > res[-1][1]:
                    res.extend(intervals[i:])
                    break
                else:
                    res[-1][1] = end
                    look_back = False
                    # discard current interval
                    continue
            if end < newInterval[0]:
                res.append(intervals[i])
            elif start <= newInterval[0] and end >= newInterval[1]:
                # merge into
                res.extend(intervals[i:])
                break
            elif start >= newInterval[0] and end > newInterval[0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                break
            elif start <= newInterval[0] and end <= newInterval[1]:
                temp = [start, newInterval[1]]
                res.append(temp)
                look_back = True
            else:
                temp = [newInterval[0], end]
                res.append(temp)

        print(f"res: {res}")
        return res