class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # sub-sequence，保证相对顺序，可以不连续
        # 也是记忆化+ dfs 的解法
        m, n = len(s), len(t)
        memo = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            # j 匹配完了，因为j+1 只发生在 s[i]==t[j] ，并选择了 s[i]的情况下
            if j == n:
                return 1
            
            # j 没有走完，但是i 走完了，说明没有匹配成功
            if i > m-1:
                return 0

            # 记忆剪枝
            if memo[i][j] != -1:
                return memo[i][j]

            count = 0

            if s[i] == t[j]:
                # 两种选择，选和不选
                count += dfs(i+1, j+1)

                count += dfs(i+1, j)

            else:
                # 只有一种选择，不选
                count += dfs(i+1, j)

            memo[i][j] = count
            return memo[i][j]

        return dfs(0, 0)