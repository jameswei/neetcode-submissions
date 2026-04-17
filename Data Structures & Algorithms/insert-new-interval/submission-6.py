class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        new_interval = newInterval

        res = list()
        # 产生了重叠，已经将new_interval和重叠的cur_interval进行了合并
        # 后序interval需要进一步检查+处理
        overlapped = False
        merged = False

        for i in range(len(intervals)):
            cur_interval = intervals[i]

            if overlapped:
                # TODO res[-1] 可能和 cur_interval 重叠
                # 消除了重叠就可以结束
                prev_end = res[-1][1]
                if prev_end < cur_interval[0]:
                    res.extend(intervals[i:])
                    break
                elif prev_end <= cur_interval[1]:
                    res[-1][1] = cur_interval[1]
                    if i < len(intervals)-1:
                        res.extend(intervals[i+1:])
                    break
                # prev_end > cur_interval[1]
                # 跳过cur_interval，继续处理重叠
                else:
                    continue

            # 1.不重叠在左侧
            if cur_interval[1] < new_interval[0]:
                res.append(cur_interval)
                continue
            
            # 3. 不重叠在右侧
            if cur_interval[0] > new_interval[1]:
                merged = True
                res.append(new_interval)
                res.extend(intervals[i:])
                break

            # 2.有重叠，直接合并进去了
            if cur_interval[0] <= new_interval[0] and cur_interval[1] >= new_interval[1]:
                merged = True
                res.extend(intervals[i:])
                break

            # 4.有重叠，需要处理
            if cur_interval[1] == new_interval[0]:
                new_start = cur_interval[0]
                new_end = new_interval[1]
                # 可能往右侵入了
                merged = True
                res.append([new_start, new_end])
                overlapped = True

            elif cur_interval[0] == new_interval[1]:
                new_start = new_interval[0]
                new_end = cur_interval[1]
                remains = intervals[i:]
                remains[0] = [new_start, new_end]
                merged = True
                res.extend(remains)
                break

            else:
                new_start = min(cur_interval[0], new_interval[0])
                new_end = max(cur_interval[1], new_interval[1])
                # 可能往右侵入了
                merged = True
                res.append([new_start, new_end])
                overlapped = True

        if not merged:
            res.append(new_interval)
        return res