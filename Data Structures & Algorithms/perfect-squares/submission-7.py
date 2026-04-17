class Solution:
    def numSquares(self, n: int) -> int:
        # perfect square就是“完全平方数”，它是一个整数的平方值

        # 先求平方根，得到一个float，向下取整后，得到[1,x]范围，只能有这个范围的数来组合
        square_root = math.sqrt(n)
        max_val = math.floor(square_root)

        INF = 2**31-1
        squares = [x**2 for x in range(1, max_val+1)]
        
        memo = [-1] * (n+1)

        # 标准记忆化+dfs
        def dfs(cur_sum: int) -> int:
            if cur_sum == n:
                return 0

            if memo[cur_sum] != -1:
                return memo[cur_sum]

            min_count = INF

            for i in range(len(squares)):
                val = squares[i]
                if cur_sum + val <= n:
                    min_count = min(min_count, 1+dfs(cur_sum+val))
                else:
                    # squares是单调递增，如果已经超出，那后面的都不需要尝试了
                    break
            
            memo[cur_sum] = min_count
            return min_count

        return dfs(0)