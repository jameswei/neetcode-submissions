class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        needed_char = {}
        for c in t:
            needed_char[c] = needed_char.get(c, 0) + 1
        
        result = ""
        satisfied = 0
        found_char = {}
        min_len = len(s)

        i, j = 0, 0

        # expand window
        while j < len(s):
            c = s[j]
            found_char[c] = found_char.get(c, 0) + 1
            if c in needed_char.keys() and found_char[c] == needed_char[c]:
                satisfied += 1
            if satisfied == len(needed_char.keys()):
                # shrink window
                while i <= j and satisfied == len(needed_char):
                    if satisfied == len(needed_char.keys()) and j - i + 1 <= min_len:
                        min_len = j - i + 1
                        result = s[i:] if j+1 >= len(s) else s[i:j+1]
                    c = s[i]
                    found_char[c] = found_char[c] - 1
                    if c in needed_char.keys() and found_char[c] == needed_char[c] - 1:
                        satisfied -= 1
                    i += 1
            j += 1

        return result