class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 变成单调增，方便剪枝
        nums.sort()

        total_sum = 0
        for n in nums:
            total_sum += n

        # 和是奇数根本没法平分成两组
        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        # res = []
        # 不用传递和维护path，因为题目不要求返回分组

        def dfs(idx: int, target_sum: int) -> bool:
            if idx > len(nums)-1:
                return False

            # 凑出来了
            if target_sum == 0:
                # res.append(path[:])
                return True

            # 剪枝
            # 也可以不用这个判断，而在递归开始时判断target_sum是不是<0，等同于越界返回
            if nums[idx] > target_sum:
                return False

            # 要么选这个数
            # path.append(nums[idx])
            if dfs(idx+1, target_sum-nums[idx]):
                return True
            # path.pop()

            # 要么不选这个数
            if dfs(idx+1, target_sum):
                return True

            # 可以合并两个递归
            return dfs(idx+1, target_sum-nums[idx]) or dfs(idx+1, target_sum)
            
            return False

        return dfs(0, half_sum)

            