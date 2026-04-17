class MinStack:

    def __init__(self):
        # 为了让 min_stack 和主栈一一对应，必须在push时也压入一个元素，同时pop时也弹出
        # min_stack 每个元素都代表到该位置为止的最小值，并不是全局最小值
        self.stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self._min_stack) == 0:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(self._min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
