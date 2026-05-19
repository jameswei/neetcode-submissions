class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        found_char_count = defaultdict(int)
        need_char_count = defaultdict(int)

        for c in s1:
            need_char_count[c] += 1

        total_need_chars = len(need_char_count)
        total_matched_chars = 0

        # [i,j)
        i, j = 0, 0
        while j < len(s2):
            
            while j-i <= len(s1):
                j += 1
                new_char = s2[j-1]
                found_char_count[new_char] += 1
                if new_char in need_char_count and found_char_count[new_char] == need_char_count[new_char]:
                    total_matched_chars += 1

            # j-i > len(s1)    
            if j-i > len(s1):
                old_char = s2[i]
                found_char_count[old_char] -= 1
                if old_char in need_char_count and found_char_count[old_char] == need_char_count[old_char]-1:
                    total_matched_chars -= 1
                i += 1

            # j-i == len(s1)
            if total_matched_chars == total_need_chars:
                return True

        return False       