class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sub-array, 要求连续、原始顺序、非空，所以不能排序
        n = len(nums)
        # [i,j) 就是滑动窗口的范围
        i, j = 0, 0
        # 窗口状态不需要维护数字个数，只需要记录sum是否满足>=target
        # 最小长度的初始值可以取2**31-1，但实际根据题目最大就是原数组长度
        sum_in_window, min_len = 0, 2**31-1

        # 因为是左闭右开窗口，所以j==n时，就包含了[n-1]元素
        while j < n:
            # 扩大窗口
            j += 1
            new_num = nums[j-1]
            sum_in_window += new_num

            if sum_in_window >= target:
                min_len = min(min_len, j-i)
            
            # 满足条件就尝试缩小窗口
            while sum_in_window > target and i < j-1:
                old_num = nums[i]
                sum_in_window -= old_num
                i += 1
                if sum_in_window >= target:
                    min_len = min(min_len, j-i)


        return min_len if min_len < 2**31-1 else 0