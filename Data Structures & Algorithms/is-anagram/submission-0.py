class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # not anagram if lenght are not equal
        if len(s) != len(t):
            return False
        s_dict = {c:0 for c in s}
        for c in s:
            s_dict[c] += 1
        t_dict = {c:0 for c in t}
        for c in t:
            t_dict[c] += 1
        for k,v in s_dict.items():
            if k not in t_dict or v != t_dict[k]:
                return False
        return True
