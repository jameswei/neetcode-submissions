class TimeMap:
    def __init__(self):
        self._map = defaultdict(list)
        

    # O(1), the given timestamps are strictly increasing
    # a simple list of (value, timestamp) pairs for every key.
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((value, timestamp))

    # O(logN), find the latest timestamp <= the given timestamp
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""
        pairs = self._map[key]
        
        # [i,j)，这里左闭右开是找到第一个超过timestamp的值，而最终结果是[i-1]
        i, j = 0, len(pairs)
        while i < j:
            mid = i + (j-i)//2
            pair = pairs[mid]

            if pair[1] <= timestamp:
                i = mid + 1
            else:
                j = mid

        # i==j
        if i == 0:
            return ""
        return pairs[i-1][0]
