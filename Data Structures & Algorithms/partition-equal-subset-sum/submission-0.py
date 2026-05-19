class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1 <= nums[i] <= 50
        # 如果 nums 中数字连续，那么可以先排序，变成连续其单调递增后，
        # 如果数字是偶数个那么就可以划分，如果是奇数个就无法划分
        # 但这里没说数字连续

        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]

        return (total_sum % 2) == 0