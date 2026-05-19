class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # k个等和子集问题，和“火柴棍凑正方形”类似
        n = len(nums)
        nums.sort(reverse=True)
        total_sum = sum(nums)
        if total_sum % k != 0 or nums[0] > total_sum // k:
            return False

        groups = [0] * k

        def dfs(i: int) -> bool:
            if i == n:
                g_sum = groups[0]
                for s in groups:
                    if s == g_sum:
                        g_sum = s
                    else:
                        return False
                return True

            for j in range(k):
                groups[j] += nums[i]
                if dfs(i+1):
                    return True
                groups[j] -= nums[i]

            return False

        return dfs(0)