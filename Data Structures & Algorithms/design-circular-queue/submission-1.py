class MyCircularQueue:
    # 环状队列，也就是常见的Ring Buffer，它有着普通队列的FIFO特点，但因为“环”存在，所以是“定长”的。
    # 当长度已满，再从尾部push进来新元素，会挤掉最旧的元素，也就相当于隐式得pop出头部元素。

    def __init__(self, k: int):
        self._capacity = k
        self._array = []
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._array.append(value)
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._array.pop(0)
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self._array[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self._array[-1]
        

    def isEmpty(self) -> bool:
        return len(self._array) == 0
        

    def isFull(self) -> bool:
        return len(self._array) == self._capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()