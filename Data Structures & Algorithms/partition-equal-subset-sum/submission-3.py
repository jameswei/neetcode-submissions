class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        nums.sort()

        total_sum = 0
        for n in nums:
            total_sum += n

        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        res = []

        def dfs(idx: int, target_sum: int, path: list[int]) -> bool:
            if idx > len(nums)-1:
                return False

            if target_sum == 0:
                res.append(path)
                return True

            if nums[idx] > target_sum:
                return False

            path.append(nums[idx])
            if dfs(idx+1, target_sum-nums[idx], path):
                return True
            path.pop()

            if dfs(idx+1, target_sum, path):
                return True
            
            return False

        print(f"res: {res}")
        return dfs(0, half_sum, [])

            