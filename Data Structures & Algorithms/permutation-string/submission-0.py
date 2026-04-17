class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 如果是找substring，隐含了“连续性”要求
        # 但是permution可以不要求保持substring的顺序

        # length 要一致
        # char 要都满足数量要求
        if len(s1) > len(s2):
            return False

        found_char_count = defaultdict(int)
        required_char_count = defaultdict(int)
        for c in s1:
            required_char_count[c] += 1

        required_chars = len(required_char_count)
        satisfied_chars = 0

        # s1="ab" s2="lecabee"
        # [i,j), [0,0) contains nothing
        i, j = 0, 0
        while j < len(s2):

            while j < len(s2) and satisfied_chars < required_chars:
                j += 1
                new_char = s2[j-1]
                found_char_count[new_char] += 1
                if new_char in required_char_count and found_char_count[new_char] == required_char_count[new_char]:
                    satisfied_chars += 1

            # either j == len(s2) or satisfied_chars == required_chars
            # "lecab"

            if j == len(s2) and satisfied_chars < required_chars:
                return False

            print(f"'{s2[i:j]}', i: {i}, j:{j}, satisfied_chars: {satisfied_chars}, required_chars: {required_chars}")

            while i < j-len(s1) and satisfied_chars == required_chars:
                old_char = s2[i]
                found_char_count[old_char] -= 1
                if old_char in required_char_count and found_char_count[old_char] == required_char_count[old_char] - 1:
                    satisfied_chars -= 1
                i += 1

            # either i == j+1 or satisfied_chars < required_chars
        
            if j-i == len(s1) and satisfied_chars == required_chars:
                return True

            print(f"'{s2[i:j]}', i: {i}, j: {j}, satisfied_chars: {satisfied_chars}, required_chars: {required_chars}")
        

        return satisfied_chars == required_chars
