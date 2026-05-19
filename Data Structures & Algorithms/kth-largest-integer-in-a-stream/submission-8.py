class KthLargest:

    # 用给定nums建一个包含k 元素的小顶堆
    # 它维护的是所有输入数字中最大的k 个
    # 其中堆定就是这k 个里最小的，也就是所有数字中第k 大的
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.size = k

        # 不确定 nums 有多少元素，既然堆大小是k，就添加k 个元素
        # [0...k-1]
        for num in nums[0:k]:
            self.heap.append(num)

        # 建堆
        if len(self.heap) > 1:
            self._heapify()

        # 剩余元素等同于add新元素
        for num in nums[k:]:
            self.add(num)

    def _heapify(self):
        # 从最后一个非叶子节点开始，一直到堆顶，往下调整
        last_parent = (len(self.heap)-1) // 2
        for i in range(last_parent, 0 , -1):
            self._sift_down_from(i)

    def _sift_down_from(self, i: int):
        # 调整所有可能破坏的子树（只要有左孩子就算子树）
        while i * 2 < len(self.heap):
            left_child = 2 * i
            right_child = 2 * i + 1
            smallest = left_child

            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
                smallest = right_child
            
            if self.heap[i] <= self.heap[smallest]:
                break
            
            # swap [i] with [swap]
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]

    def add(self, val: int) -> int:
        # 堆还没有满，直接加入
        if len(self.heap)-1 < self.size:
            self.heap.append(val)

            # 从最后一个元素（新元素）开始向上调整
            i = len(self.heap)-1
            self._sift_up_from(i)
        # 堆已满
        else:
            if val <= self.heap[1]:
                # 新的数太小了，直接丢掉，返回现在的堆顶
                return self.heap[1]
        
            self.heap[1] = val
            self._sift_down_from(1)

        return self.heap[1]

    def _sift_up_from(self, i: int):
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2
