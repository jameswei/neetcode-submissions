class MedianFinder:

    def __init__(self):
        # 两个heap
        # 一个大顶堆用来放较小的一半，它的堆顶就是较小数中最大的
        # 一个小顶堆用来放较大的一半，它的堆顶就是较大数中最小的
        # 大顶堆用heapq时需要以负值来实现

        self.min_heap, self.max_heap = [], [] 

    # input num is sorted integer
    # later one is always bigger than the early one
    def addNum(self, num: int) -> None:
        if len(self.max_heap)>0 and num > self.max_heap[0]*(-1):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num*(-1))

        # re-balance 2 heaps
        if len(self.min_heap) > len(self.max_heap)+1:
            # 把 min_heap 的堆顶取出放入 max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val*(-1))
        
        if len(self.max_heap) > len(self.min_heap)+1:
            val = heapq.heappop(self.max_heap)*(-1)
            heapq.heappush(self.min_heap, val)

        
    # 两个heap 元素数：
    # 如果奇数，从较多的堆中取堆顶，即是结果
    # 如果偶数，从两个堆中各取堆顶，求算术平均数，即是结果
    def findMedian(self) -> float:
        total_num = len(self.min_heap) + len(self.max_heap)
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]*(-1)
        else:
            return (self.max_heap[0]*(-1)+self.min_heap[0])/2

                
        