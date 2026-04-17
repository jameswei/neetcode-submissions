class DynamicArray:
    
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        # technically python's list is already dynamic
        self._arr: list[Optional[int]] = [None] * self._capacity

    def get(self, i: int) -> int | None:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        
        # insert() function is not allowed and it doest meet O(1)
        self._arr[self._size] = n
        self._size += 1

    def popback(self) -> int | None:
        popped = self._arr[self._size-1]
        self._arr[self._size-1] = None
        self._size -= 1
        return popped

    def resize(self) -> None:
        # double the original capacity and extend the underlying array
        # i think extend() and append() are not allowed
        self._capacity *= 2
        new_arr: list[Optional[int]] = [None] * self._capacity

        for i in range(self._size):
            new_arr[i] = self._arr[i]
        
        self._arr = new_arr

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self._capacity
