class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total_sum = 0
        for num in nums:
            total_sum += num

        if target < -1*total_sum or target > total_sum:
            return 0
        
        # dp[i][j] 使用[0,i-1]个数，凑出j 的方式
        # 注意！target可能是负数，那为了确保j>=0满足数组索引的要求，需要归一到正数范围
        # 但是整个nums[]计算的上下限是[-total_sum, total_sum]，也就是全为负数求和到全为正数求和。
        # 为了归一到数组索引区间，offset就是total_sum
        offset = total_sum
        dp = [[0] * (2*total_sum+1) for _ in range(n+1)]
        # dp[0][x]肯定都是0，相当于不使用任何数，毛线也凑不出来
        # 例外是dp[0][0]，不用任何数，凑出0，有1种，题目要求是“保持顺序且都使用”
        dp[0][0+offset] = 1

        for i in range(1, len(dp)):
            num = nums[i-1]
            for j in range(len(dp[i])):
                # 要求必须得用 num
                # 所以要么前面的结果是j-num，这时候+num才能凑上j
                # 要么前面的结果是j+num，这是-num才能凑上j
                # 再考虑到target值被映射到>=0范围，所以都需要再加上offet
                if j-num >= 0:
                    dp[i][j] += dp[i-1][j-num]
                if j+num < 2*total_sum+1:
                    dp[i][j] += dp[i-1][j+num]

        return dp[n][target+offset]