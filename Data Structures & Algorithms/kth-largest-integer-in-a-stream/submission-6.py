class KthLargest:

    # 用给定nums建一个包含k 元素的小顶堆
    # 它维护的是所有输入数字中最大的k 个
    # 其中堆定就是这k 个里最小的，也就是所有数字中第k 大的
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.size = k

        if len(nums) > k:
            self.heap.extend(nums[0:k])
            over_sized_nums = nums[k:]
            print(f"heap: {self.heap}, over_sized: {over_sized_nums}")

            self._heapify()
            for num in over_sized_nums:
                self.add(num)

        else:
            self.heap.extend(nums)
            print(f"heap: {self.heap}")
            self._heapify()


    def _heapify(self):
        # parent of last element = (last element) / 2
        last_parent = (len(self.heap)-1) // 2
        cur = last_parent
        
        # from last parent backward to first element [1]
        while cur > 0:
            i = cur
            
            # 调整所有可能破坏的子树
            while i*2 < len(self.heap):
                if len(self.heap) > (i*2+1) and self.heap[i*2+1] < self.heap[i*2] and self.heap[i] > self.heap[i*2+1]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i*2+1]
                    self.heap[i*2+1] = temp
                    i = i*2+1
                elif self.heap[i] > self.heap[i*2]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i*2]
                    self.heap[i*2] = temp
                    i = i*2
                else:
                    break

            cur -= 1
        
        print(f"heap: {self.heap}")


    def add(self, val: int) -> int:
        if len(self.heap) > 1 and val <= self.heap[1]:
            # 新的数太小了，直接丢掉，返回现在的堆顶
            return self.heap[1]
        
        # 踢出旧的堆顶，新的数放在堆顶，进行sift-down，最终新的堆顶就是第k大的数
        if len(self.heap) > 1:
            self.heap[1] = val
            self._sift_down()
        else:
            self.heap.append(val)

        return self.heap[1]

    def _sift_down(self):
        print(f"before sift down: {self.heap}")
        last_parent = (len(self.heap)-1) // 2

        cur = 1

        while cur <= last_parent:
            i = cur

            while 2*i < len(self.heap):
                if 2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2*i+1]
                    self.heap[2*i+1] = temp
                    i = 2*i+1
                elif self.heap[i] > self.heap[2*i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = temp
                    i = i*2
                else:
                    break

            cur += 1

        print(f"after sift down: {self.heap}")



