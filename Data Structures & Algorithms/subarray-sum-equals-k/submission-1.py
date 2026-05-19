class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 找subarray，第一要求是 contiguous！连续性
        # dfs的方式通常解决subset问题

        n = len(nums)
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        
        cur_sum = 0
        total_count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            prefix_sum_count[cur_sum] += 1

            total_count += prefix_sum_count[cur_sum - k]


        return total_count

