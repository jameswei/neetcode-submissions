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
        min_len = float('inf')

        # j will go to len(s), [i,j) is result
        i, j = 0, 0

        # expand window
        while j < len(s):
            c = s[j]
            j += 1
            found_char[c] = found_char.get(c, 0) + 1
            if c in needed_char.keys() and found_char[c] == needed_char[c]:
                satisfied += 1

            # found an answer and shrink window
            while satisfied == len(needed_char):
                if j - i < min_len:
                    min_len = j - i
                    result = s[i:j]

                c = s[i]
                i += 1
                found_char[c] = found_char[c] - 1
                if c in needed_char.keys() and found_char[c] == needed_char[c] - 1:
                    satisfied -= 1

        return result