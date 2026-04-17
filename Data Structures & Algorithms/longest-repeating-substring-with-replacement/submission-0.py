class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        longest = 0
        char_to_count = dict()
        most_char_count = 0
        i, j = 0, 0
        while j < len(s):
            added_char = s[j]
            char_to_count[added_char] = char_to_count.get(added_char, 0) + 1
            most_char_count = max(most_char_count, char_to_count[added_char])

            while (j - i + 1) - most_char_count > k:
                removed_char = s[i]
                char_to_count[removed_char] = char_to_count[removed_char] - 1
                most_char_count = max(most_char_count, char_to_count[removed_char])
                i += 1
            
            longest = max(longest, j - i + 1)
            j += 1
        
        return longest
