class MinStack:

    def __init__(self):
        self.stack = list()
        # a monotonical stack, min val is on the top
        self._min_stack = list()
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self._min_stack) == 0 or val <= self._min_stack[-1]:
            self._min_stack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self._min_stack[-1]:
            self._min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
