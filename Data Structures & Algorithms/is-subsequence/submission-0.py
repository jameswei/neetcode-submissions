class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0

        while i < m and j < n:
            s_char = s[i]
            t_char = t[j]

            if s_char == t_char:
                i += 1

            j += 1

        return i == m