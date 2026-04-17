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

            if optimistic < 0:
                return False
            if pessimistic < 0:
                pessimistic = max(0, pessimistic)

        return pessimistic == 0