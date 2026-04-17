class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) <= 1:
            return len(s)

        char_to_count = dict()
        # length >= 2
        longest = 1
        # [l,r]
        l, r = 0, 0
        while r < len(s):
            added_c = s[r]
            char_to_count[added_c] = char_to_count.get(added_c, 0) + 1

            while char_to_count[added_c] > 1:
                removed_c = s[l]
                char_to_count[removed_c] = char_to_count[removed_c] - 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest