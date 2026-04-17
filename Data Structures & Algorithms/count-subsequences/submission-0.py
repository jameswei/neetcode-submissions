class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # sub-sequence，保证相对顺序，可以不连续
        # 感觉也是记忆化+ dfs 的解法
        m, n = len(s), len(t)
        memo = [[-1] * n for _ in range(m)]
        
        all_subsequences = []

        def dfs(i: int, j: int, path: list[int]) -> int:
            if len(path) == len(t):
                print(f"found a subsequence: {path[:]}")
                all_subsequences.append(path[:])
                return 1
            
            if i > m-1 or j > n-1:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            s_char, t_char = s[i], t[j]
            count = 0
            if s_char == t_char:
                # 两种选择，选和不选
                path.append(i)
                count += dfs(i+1, j+1, path)
                path.pop()

                count += dfs(i+1, j, path)

            else:
                # 只有一种选择，不选
                count += dfs(i+1, j, path)

            memo[i][j] = count

            return memo[i][j]


        return dfs(0, 0, [])