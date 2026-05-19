class MyCircularQueue:
    # 环状队列，也就是常见的Ring Buffer，它有着普通队列的FIFO特点，但因为“环”存在，所以是“定长”的。
    # 当长度已满，再从尾部push进来新元素，会挤掉最旧的元素，也就相当于隐式得pop出头部元素。

    def __init__(self, k: int):
        self._capacity = k
        self._array = [-1] * k
        self._front = 0
        self._rear = 0
        self._size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self._array[self._rear] = value
        self._rear = (self._rear+1) % self._capacity
        self._size += 1

        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        _ = self._array[self._front]
        self.front = (self._front+1) % self._capacity
        self._size -= 1

        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self._array[self._front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self._array[(self._rear-1)]
        

    def isEmpty(self) -> bool:
        return self._size == 0
        

    def isFull(self) -> bool:
        return self._size == self._capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()