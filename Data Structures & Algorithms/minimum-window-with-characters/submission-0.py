class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # char in 't' -> occurrence count
        char_to_count = {}
        for c in t:
            char_to_count[c] = char_to_count.get(c, 0) + 1

        min_len = len(s)
        result = ""
        i = 0
        while i < len(s):
            j = i
            # reset state
            total_count = len(t)
            count = char_to_count.copy()

            while j < len(s) and total_count > 0:
                c = s[j]
                if c in count.keys():
                    count[c] = count[c] - 1
                    if count[c] == 0:
                        total_count -= 1
                j += 1

            if total_count == 0 and j - 1 <= min_len:
                result = s[i:j]

            i += 1

        return result