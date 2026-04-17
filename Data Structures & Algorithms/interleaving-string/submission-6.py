class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m+n != o:
            return False

        memo = {}

        # i, j, k 分别是s1，s2，s3 的索引
        def dfs(i: int, j:int, k: int) -> bool:
            if i == m and j == n and k == o:
                return True

            if (i, j) in memo:
                return memo[(i,j)]

            s3_char = s3[k]

            # s3 中的字符只能来自于s1 或s2
            match = False

            # 和s1 字符相同
            if i < m and s3_char == s1[i]:
                match = match or dfs(i+1, j, k+1)
            
            # 和s2 字符相同
            if j < n and s3_char == s2[j]:
                match = match or dfs(i, j+1, k+1)

            memo[(i,j)] = match
            return match

        return dfs(0, 0, 0)