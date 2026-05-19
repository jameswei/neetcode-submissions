class Solution:
    def numSquares(self, n: int) -> int:
        # perfect square就是“完全平方数”，它是一个整数的平方值

        # 先求平方根，得到一个float，向下取整后，得到[1,x]范围，只能有这个范围的数来组合
        square_root = math.sqrt(n)
        max_val = math.floor(square_root)

        possible_nums = [x for x in range(1, max_val+1)]
        memo = [[0] * len(possible_nums) for _ in range(n+1)]
        # 标准记忆化+dfs
        def dfs(i: int, cur_sum: int, path: list[int]) -> int:

            if cur_sum == n:
                return len(path)

            if memo[cur_sum][i] != 0:
                return memo[cur_sum][i]
            
            min_count = 2**31-1
            for j in range(i, len(possible_nums)):
                val = possible_nums[j]**2
                if cur_sum + val <= n:
                    path.append(val)
                    min_count = min(min_count, dfs(j, cur_sum+val, path))
                    path.pop()
                else:
                    # possible_nums是单调递增，如果nums[i]已经超出，那后面的都不需要尝试了
                    break
                
            memo[cur_sum][i] = min_count
            return min_count

        return dfs(0, 0, [])