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

        # 如果整个数组都是负数，那么total_sum一定是负数，那么最小的子数组和一定也是负数，并且这个子数组就是原始本身
        # 那么total_sum-min_sum==0，此时和同样情况下计算的最大的子数组和求最大，会始终返回0
        if total_sum < 0:
            return max_sum_linear

        # 这里total_sum-min_sum_linear表示在线性数字中最小的子数组和的情况下，剩下的补集也就是发生回转的字数组会有最大的和
        return max(max_sum_linear, total_sum-min_sum_linear)