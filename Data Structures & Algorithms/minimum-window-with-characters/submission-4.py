class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        result = ""

        total_count = len(t)
        char_to_count = {}
        for c in t:
            char_to_count[c] = char_to_count.get(c, 0) + 1
        min_len = len(s)

        i, j = 0, 0

        while i < len(s):

            # expand the window
            while j < len(s) and total_count > 0:
                c = s[j]
                if c in char_to_count.keys():
                    char_to_count[c] = char_to_count[c] - 1
                    if char_to_count[c] >= 0:
                        total_count -= 1
                j += 1
            if total_count > 0:
                # no result
                break
            
            if j - i <= min_len:
                result = s[i:j]
                min_len = j - i

            # shrink the window
            while i < j and total_count == 0:
                c = s[i]
                if c in char_to_count.keys():
                    char_to_count[c] = char_to_count[c] + 1
                    if char_to_count[c] > 0:
                        total_count += 1
                i += 1

            if j - i + 1 <= min_len:
                result = s[i-1:j]
                min_len = j - i + 1

        return result