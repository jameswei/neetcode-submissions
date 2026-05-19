class Solution:
    def validPalindrome(self, s: str) -> bool:
        stack = []

        for c in s:
            stack.append(c)

        count = 0
        for c in s:
            if c != stack.pop():
                count += 1
            
        return count == 0 or count == 2