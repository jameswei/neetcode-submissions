class StockSpanner:

    def __init__(self):
        self._stack = []
        self._temp_stack = []
        

    # 栈里<=price的个数+1，回看有几天不大于今天的price，返回个数+1，意思是这个price是几天内的最大值
    def next(self, price: int) -> int:
        days = 1
        while len(self._stack) > 0 and self._stack[-1] <= price:
            self._temp_stack.append(self._stack.pop())
            days += 1

        while len(self._temp_stack) > 0:
            self._stack.append(self._temp_stack.pop())

        self._stack.append(price)
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)