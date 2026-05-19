class Solution:
    def validPalindrome(self, s: str) -> bool:
        stack = []

        for c in s:
            stack.append(c)

        count = 0
        for c in s:
            if c != stack.pop():
                count += 1
                if count > 2:
                    return False
            
        return True