class Solution:
    def numSquares(self, n: int) -> int:
        # perfect square就是“完全平方数”，它是一个整数的平方值

        # 先求平方根，得到一个float，向下取整后，得到[1,x]范围，只能有这个范围的数来组合
        square_root = math.sqrt(n)
        max_val = math.floor(square_root)

        possible_nums = [x for x in range(1, max_val+1)]

        res = 2**31-1
        # 找符合条件的解，同时要求解中包含的数值最少
        def dfs(cur_sum: int, path: list[int]):
            nonlocal res

            if cur_sum == n:
                res = min(res, len(path))
                return
            
            for i in range(len(possible_nums)):
                val = possible_nums[i]**2
                if cur_sum + val <= n:
                    path.append(val)
                    dfs(cur_sum+val, path)
                    path.pop()
                
            return

        dfs(0, [])
        return res