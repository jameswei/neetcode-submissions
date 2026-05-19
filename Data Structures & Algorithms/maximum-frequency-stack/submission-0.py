class FreqStack:

    def __init__(self):
        # (frequency, index, value)
        self._heap = []
        self._indexer = 0
        self._counter = {}

    def push(self, val: int) -> None:
        if val not in self._counter:
            self._counter[val] = 1
        else:
            self._counter[val] += 1

        heapq.heappush(self._heap, (-1*self._counter[val], -1*self._indexer, val))
        self._indexer += 1
        

    # pop the most frequent element
    # 说明要有个结构来维护出现的frequency，在pop时以此作为第一条件
    # 如果有frequency相同的元素，那pop离栈顶更近的，所以还要有个结构来维护元素的位置
    def pop(self) -> int:
        _, _, val = heapq.heappop(self._heap)
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()