class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0

        res = []

        while i < m and j < n:
            res.append(word1[i])
            i += 1
            res.append(word2[j])
            j += 1


        if i < m:
            res.append(word1[i:])
        
        if j < n:
            res.append(word2[j:])

        return ''.join(res)