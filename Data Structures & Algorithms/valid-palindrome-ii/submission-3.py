class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        
        def is_palindrome(i: int, j: int, count: int) -> bool:
            if count > 1:
                return False
            if i >= j:
                return True

            if s[i] == s[j]:
                return is_palindrome(i+1, j-1, count)
            else:
                return is_palindrome(i+1, j, count+1) or is_palindrome(i, j-1, count+1)

        return is_palindrome(start, end, 0)