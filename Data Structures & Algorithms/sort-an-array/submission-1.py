class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        # 计数排序解法
        num_count = defaultdict(int)
        min_num, max_num = 2*31-1, -2**31

        for n in nums:
            min_num = min(min_num, n)
            max_num = max(max_num, n)
            num_count[n] += 1

        i = 0
        for k in range(min_num, max_num+1):
            if num_count[k] > 0:
                for _ in range(num_count[k]):
                    nums[i] = k
                    i += 1

        return nums