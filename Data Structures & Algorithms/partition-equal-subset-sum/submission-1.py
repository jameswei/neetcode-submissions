class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1 <= nums[i] <= 50
        # 如果 nums 中数字连续，那么可以先排序，变成连续其单调递增后，
        # 如果数字是偶数个那么就可以划分，如果是奇数个就无法划分
        # 但这里没说数字连续
        
        total_sum = 0
        for n in nums:
            total_sum += n

        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        def dfs(idx: int, target_sum: int, sub_set: list[int]):
            if idx > len(nums)-1:
                return
            if nums[idx] > target_sum:
                return
            
            if nums[idx] == target_sum:
                sub_set.append(nums[idx])
                return

            sub_set.append(nums[idx])
            dfs(idx+1, target_sum-nums[idx], sub_set)
            sub_set.pop()

        res = []
        for i in range(len(nums)):
            sub_set = list()
            dfs(i, half_sum, sub_set)
            if len(sub_set) > 0:
                res.append(sub_set)

        return len(res) > 0