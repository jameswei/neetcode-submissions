class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            # only itself
            return 1
        
        total = 0

        # a len*len matrix
        is_palindrome = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):

                if i == j:
                    is_palindrome[i][j] = True
                
                elif i+1 == j:
                    is_palindrome[i][j] = s[i] == s[j]

                else:
                    if i+1 > len(s)-1 or j-1 < 0:
                        is_palindrome[i][j] = False
                    else:
                        is_palindrome[i][j] = is_palindrome[i+1][j-1] and s[i] == s[j]
                
                if is_palindrome[i][j]:
                    total += 1

        return total