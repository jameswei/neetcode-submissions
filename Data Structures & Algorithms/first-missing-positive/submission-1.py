class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 找最小的没出现的正数
        min_val, max_val = 2**31-1, -2**31
        num_count = defaultdict(int)

        for n in nums:
            min_val = min(min_val, n)
            max_val = max(max_val, n)
            num_count[n] += 1

        if min_val > 1 or max_val <= 0:
            return 1

        for k in range(min_val, max_val+1):
            if k > 0 and num_count[k] == 0:
                return k

        return max_val+1