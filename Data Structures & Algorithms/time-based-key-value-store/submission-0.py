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

        if len(pairs) == 1:
            return pairs[0][0]
        
        val = ""
        i, j = 0, len(pairs)-1
        while i <= j:
            mid = i + (j-i)//2
            pair = pairs[mid]

            if pair[1] <= timestamp:
                val = pair[0]
                i = mid + 1
            else:
                j = mid - 1

        return val
