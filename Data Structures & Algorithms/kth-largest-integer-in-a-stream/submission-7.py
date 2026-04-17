class KthLargest:

    # 用给定nums建一个包含k 元素的小顶堆
    # 它维护的是所有输入数字中最大的k 个
    # 其中堆定就是这k 个里最小的，也就是所有数字中第k 大的
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.size = k

        for num in nums[:k]:
            self.heap.append(num)

        if len(self.heap) > 1:
            self._heapify()

        for num in nums[k:]:
            self.add(num)

    def _sift_down_from(self, i: int):
        # 调整所有可能破坏的子树
        while i*2 < len(self.heap):
            left_child = 2 * i
            right_child = 2 * i + 1
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child] and self.heap[i] > self.heap[right_child]:
                temp = self.heap[i]
                self.heap[i] = self.heap[right_child]
                self.heap[right_child] = temp
                i = right_child
            elif self.heap[i] > self.heap[left_child]:
                temp = self.heap[i]
                self.heap[i] = self.heap[left_child]
                self.heap[left_child] = temp
                i = left_child
            else:
                break

    def _sift_up_from(self, i: int):
        while i > 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = temp

    def _heapify(self):
        # parent of last element = (last element) / 2
        last_parent = (len(self.heap)-1) // 2
        for i in range(last_parent, 0 , -1):
            self._sift_down_from(i)

    def add(self, val: int) -> int:
        if len(self.heap)-1 < self.size:
            # 堆还没有满，直接加入
            self.heap.append(val)
            i = len(self.heap)-1
            while i > 1:
                self._sift_up_from(i)
                i = i // 2
        else:
            # 堆已满
            if val <= self.heap[1]:
                # 新的数太小了，直接丢掉，返回现在的堆顶
                return self.heap[1]
        
            self.heap[1] = val
            self._sift_down_from(1)

        return self.heap[1]
