class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        # 堆排序解法

        def heapify(size: int):
            start = (size-1) // 2

            # [0]不用管了
            for i in range(start, 0, -1):
                percolate(size, i)
            return

        def percolate(size: int, i: int):
            l_n, r_n = 2*i, 2*i+1

            if r_n < size and nums[r_n] > nums[l_n] and nums[r_n] > nums[i]:
                nums[r_n], nums[i] = nums[i], nums[r_n]
                percolate(size, r_n)
            elif l_n < size and nums[l_n] > nums[i]:
                nums[l_n], nums[i] = nums[i], nums[l_n]
                percolate(size, l_n)

        def heap_sort():
            # 为了方便计算索引 2n 和 2n+1，把[0]挪到末尾
            nums.append(nums[0])
            nums[0] = 2**31-1

            size = len(nums)
            heapify(size)

            for i in range(size-1, 1, -1):
                nums[1], nums[i] = nums[i], nums[1]
                percolate(i, 1)

        heap_sort()
        return nums[1:]