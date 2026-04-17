class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 用Kadane算法，它是解决线性数组最大子数组和问题的好办法，对于环形数组需要些变形

        n = len(nums)
        # max_sum_linear是不考虑环形数组特点，最大的子数组和
        max_sum_linear = cur_sum = nums[0]
        total_sum = sum(nums)

        # 标准Kadane实现
        for i in range(1, n):
            num = nums[i]
            cur_sum = max(num, cur_sum+num)
            max_sum_linear = max(max_sum_linear, cur_sum)
        
        # 同样不考虑环形数组特点，最小的子数组和
        min_sum_linear = cur_sum = nums[0]
        for i in range(1, n):
            num = nums[i]
            cur_sum = min(num, cur_sum+num)
            min_sum_linear = min(min_sum_linear, cur_sum)

        if total_sum < 0:
            return max_sum_linear
            
        return max(max_sum_linear, total_sum-min_sum_linear)