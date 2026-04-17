class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        prefix = []
        i = 0

        while True:
            if i > len(strs[0])-1:
                break
            
            c = strs[0][i]

            matched = True
            for j in range(n):
                if i > len(strs[j])-1 or strs[j][i] != c:
                    matched = False
                    break
            
            if matched:
                prefix.append(c)
                i += 1
            else:
                break

        return "".join(prefix)