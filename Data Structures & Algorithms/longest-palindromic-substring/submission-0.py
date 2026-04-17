class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        # `s` contains only digits and English letters
        
        # a len(s)*len(s) matrix
        # [i][j] means if s[i:j+1] is a palindromic string
        # but the down-left part is useless, since the i>j, it's not a valid string
        is_palindrome = [[False] * len(s) for _ in range(len(s))] 
        
        longest_len = 0
        res = ""

        # fill the state
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):

                # a single char is palindromic string
                if i == j:
                    is_palindrome[i][j] = True
                
                # len==2
                elif i+1 == j:
                    is_palindrome[i][j] = s[i] == s[j]
                
                else:
                    if i+1 > len(s)-1 or j-1 < 0:
                        is_palindrome[i][j] = False
                    else:
                        is_palindrome[i][j] = is_palindrome[i+1][j-1] and s[i] == s[j]
                
                if is_palindrome[i][j] and (j-i+1) > longest_len:
                    longest_len = j-i+1
                    res = s[i:j+1]
    

        return res