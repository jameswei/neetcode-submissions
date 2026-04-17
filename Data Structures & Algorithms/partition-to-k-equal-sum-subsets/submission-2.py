class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # k个等和子集问题，和“火柴棍凑正方形”类似
        n = len(nums)
        # 递减排序
        nums.sort(reverse=True)
        total_sum = sum(nums)

        if total_sum % k != 0 or nums[0] > total_sum // k:
            return False

        target_sum = total_sum // k

        groups = [0] * k

        def dfs(i: int) -> bool:
            if i == n:
                for s in groups:
                    if s != target_sum:
                        return False
                return True

            for j in range(k):
                if groups[j] + nums[i] > target_sum:
                    continue
                if j > 0 and groups[j] >= groups[j-1]:
                    continue
                
                groups[j] += nums[i]
                if dfs(i+1):
                    return True
                groups[j] -= nums[i]

                if groups[j] == 0:
                    break

            return False

        return dfs(0)