class MyStack:

    # 要求只用FIFO的queue来实现LIFO特性，所以不能直接用stack结构
    def __init__(self):
        self._queue_1 = deque()

    def push(self, x: int) -> None:
        self._queue_1.append(x)

    def pop(self) -> int:
        l = len(self._queue_1)
        for _ in range(l-1):
            self._queue_1.append(self._queue_1.popleft())
        
        return self._queue_1.popleft()

    def top(self) -> int:
        return self._queue_1[-1]

    def empty(self) -> bool:
        return len(self._queue_1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()