class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 环形数组就是索引n-1的下一个是0，索引0的前一个是n-1，不会越界。所以
        # 所以往后移动，[i]的下一个元素：[(i+1)%n]
        # 但是往前移动，[i]的前一个元素：[(i-1+n)%n]，因为i-1可能得到负数（它本身也是合法的索引值），先+n使它变成正数，再取模

        # 要求返回符合条件的非空subarray，不可重复选，要是连续元素
        # 但对于环形数组，“连续”的情况就可以从数组尾部绕回到头部，
        # 比如[a,b,c,d,e]，其中[a,b,d,e]是合法的subarray，因为选择范围是d-e-a-b
        n = len(nums)
        # 前缀和
        prefix_sum = [0] * n
        for i in range(n):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = nums[i]+prefix_sum[i-1]

        # 后缀和
        surfix_sum = [0] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                surfix_sum[i] = nums[i]
            else:
                surfix_sum[i] = nums[i]+surfix_sum[i+1]
        MIN_INF = -2**31
        max_subarr_sum = MIN_INF

        for i in range(n):
            for j in range(i, n):
                subarr_sum_1 = prefix_sum[j]-(prefix_sum[i-1] if i>0 else 0)
                subarr_sum_2 = MIN_INF if (j-i+1==n) else (surfix_sum[j+1] if j<(n-1) else 0) + (prefix_sum[i-1] if i>0 else 0)

                max_subarr_sum = max(max_subarr_sum, subarr_sum_1, subarr_sum_2)
        
        return max_subarr_sum