class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        for n in nums:
            total_sum += n

        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        res = []

        def dfs(idx: int, target_sum: int, sub_set: list[int]):
            if idx > len(nums)-1:
                return

            if nums[idx] == target_sum:
                sub_set.append(nums[idx])
                res.append(sub_set)
                return

            # 2 options: select or not
            if nums[idx] < target_sum:
                sub_set.append(nums[idx])
                dfs(idx+1, target_sum-nums[idx], sub_set)
                sub_set.pop()
            
            dfs(idx+1, target_sum, sub_set)
            

        dfs(0, half_sum, [])
        
        return len(res) > 0