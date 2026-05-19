class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = list()
        
        # intervals=[[1,2],[3,5],[9,10]]
        # newInterval=[6,7]

        look_back = False
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if look_back:
                if start > res[-1][1]:
                    res.extend(intervals[i:])
                    break
                else:
                    res[-1][1] = end
                    look_back = True
                    continue
            if end < newInterval[0]:
                res.append(intervals[i])
            elif start > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                break
            else:
                if end > newInterval[1]:
                    # new_interval is merged
                    res.extend(intervals[i:])
                    break
                else:
                    # overlapping
                    res.append([start, newInterval[1]])
                    look_back = True

        print(f"res: {res}")
        return res