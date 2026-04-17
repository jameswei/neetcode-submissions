class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        sorted_strs = sorted(strs)
        min_len = min(len(sorted_strs[0]), len(sorted_strs[-1]))

        for i in range(min_len):
            if sorted_strs[0][i] != sorted_strs[-1][i]:
                return sorted_strs[0][:i]

        return sorted_strs[0]