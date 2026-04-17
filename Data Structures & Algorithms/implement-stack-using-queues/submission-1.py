class MyStack:

    # 嵌套queue的解法，可以保证所有操作时间复杂度O(1)
    # 原理是对于每个元素，并不是直接以值本身入队列/出队列，而是包在一个queue里，之后再将这个单元素的小queue入队列
    # 这个本质上等同于linkedlist
    def __init__(self):
        self._queue = None

    def push(self, x: int) -> None:
        self._queue = deque([x, self._queue])

    def pop(self) -> int:
        x = self._queue.popleft()
        self._queue = self._queue.popleft()

        return x

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return self._queue is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()