class LRUCache:

    def __init__(self, capacity: int):
        self._map = {}
        self._capacity = capacity
        self._queue = deque()


    # O(1)
    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        else:
            temp = []
            while self._queue[0] != key:
                cur = self._queue.popleft()
                temp.append(cur) 

            self._queue.popleft()
            while len(self._queue) > 0:
                temp.append(self._queue.popleft())
            
            self._queue.extend(temp)
            self._queue.append(key)
            return self._map[key]

    # O(1)
    def put(self, key: int, value: int) -> None:
        if key not in self._map:
            # self.size >= self._capacity
            while len(self._queue) >= self._capacity:
                k = self._queue.popleft()
                self._map.pop(k)

            self._queue.append(key)
            self._map[key] = value
        else:
            self._map[key] = value
            temp = []
            while self._queue[0] != key:
                cur = self._queue.popleft()
                temp.append(cur) 

            self._queue.popleft()
            while len(self._queue) > 0:
                temp.append(self._queue.popleft())
            
            self._queue.extend(temp)
            self._queue.append(key)
        