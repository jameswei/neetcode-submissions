class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            offset = columnNumber % 26
            res += chr(ord('A') + offset - 1)
            columnNumber //= 26

        return ''.join(reversed(res))