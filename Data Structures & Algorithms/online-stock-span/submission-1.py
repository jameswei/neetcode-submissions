class StockSpanner:
    # 本质要设计实现一个单调栈 monotonic stack
    # 单调栈适用的场景就是“范围查询”

    def __init__(self):
        # 栈中数据(price, span_days)
        self._mono_stack = []
        

    def next(self, price: int) -> int:
        days = 1

        # 栈不为空，栈顶price低于当前price
        while len(self._mono_stack) > 0 and self._mono_stack[-1][0] <= price:
            # 弹出比当前price低的，并抛弃
            prev_price, span = self._mono_stack.pop()
            days += span
        
        self._mono_stack.append((price, days))
        return days



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)