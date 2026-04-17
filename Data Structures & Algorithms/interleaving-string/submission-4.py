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
            
            # 由于不匹配，s1 和s2 都走完了
            if i == m and j == n:
                return False

            if (i, j) in memo:
                return memo[(i,j)]

            s3_char = s3[k]

            match = False
            if i < m and s3_char == s1[i]:
                match = match or dfs(i+1, j, k+1)
            
            if j < n and s3_char == s2[j]:
                match = match or dfs(i, j+1, k+1)
            
            if match:
                return True

            memo[(i,j)] = match
            return False

        return dfs(0, 0, 0)