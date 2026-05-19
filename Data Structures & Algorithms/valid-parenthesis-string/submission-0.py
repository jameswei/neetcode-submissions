class Solution:
    def checkValidString(self, s: str) -> bool:
        optimistic = 0
        pessimistic = 0

        for char in s:
            if char == "(":
                pessimistic += 1
                optimistic += 1
            elif char == ")":
                pessimistic -= 1
                optimistic -= 1
            else:
                optimistic += 1
                pessimistic -= 1

        return pessimistic <= 0