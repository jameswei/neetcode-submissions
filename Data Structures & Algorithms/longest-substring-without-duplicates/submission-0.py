class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_to_count = dict()
        duplicated_char = 0

        longest = 0
        # (b,e]
        b, e = -1, 0

        while b < e and e < len(s):
            # e moves forward to add char til duplicated was found
            while e < len(s):
                c = s[e]
                cnt = char_to_count.get(c, 0) + 1
                char_to_count[c] = cnt
                if cnt > 1:
                    # duplicated char was found
                    duplicated_char += 1
                    # stop here
                    break
                else:
                    e += 1

            # b moves forward to remove char till duplicated was removed
            while b < e and duplicated_char > 0:
                b += 1
                c = s[b]
                cnt = char_to_count[c] - 1
                char_to_count[c] = cnt
                if cnt == 1:
                    duplicated_char -= 1

            longest = max(longest, e - (b + 1) + 1)
            e += 1

        return longest