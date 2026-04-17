class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_to_pos = dict()
        longest_len = 1
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            if c in char_to_pos and char_to_pos[c] >= l:
                # duplicated char, move left
                l = char_to_pos[c] + 1
            char_to_pos[c] = r
            longest_len = max(longest_len, r - l + 1)
            r += 1
        return longest_len
