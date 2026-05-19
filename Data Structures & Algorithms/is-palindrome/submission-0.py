import string

class Solution:
    # def is_alpha_numeric(ch: str) -> bool:
    #     return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        i, j = 0, len(s)-1
        while i <= j:
            while s[i] not in (string.ascii_letters + string.digits) and i <= j:
                i += 1
            while s[j] not in (string.ascii_letters + string.digits) and j >= i:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False

        return True