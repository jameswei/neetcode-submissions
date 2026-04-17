class Solution:
    def numSquares(self, n: int) -> int:
        # perfect square就是“完全平方数”，它是一个整数的平方值

        # 先求平方根，得到一个float，向下取整后，得到[1,x]范围，只能有这个范围的数来组合
        square_root = math.sqrt(n)
        max_val = math.floor(square_root)

        INF = 2**31-1
        possible_nums = [x for x in range(1, max_val+1)]
        memo = [[0] * len(possible_nums) for _ in range(n+1)]

        # 标准记忆化+dfs
        def dfs(i: int, remaining_sum: int) -> int:
            if remaining_sum == 0:
                return 0

            if memo[remaining_sum][i] != 0:
                return memo[remaining_sum][i]

            min_count = INF
            for j in range(i, len(possible_nums)):
                val = possible_nums[j]**2
                if val <= remaining_sum:
                    min_count = min(min_count, 1+dfs(j, remaining_sum-val))
                else:
                    # possible_nums是单调递增，如果nums[i]已经超出，那后面的都不需要尝试了
                    break
                
            memo[remaining_sum][i] = min_count
            return min_count

        return dfs(0, n)