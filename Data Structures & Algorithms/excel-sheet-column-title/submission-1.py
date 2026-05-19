class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        start = ord('A')-1
        res = []
        while columnNumber // 26 > 0:
            res.append(chr(start + (columnNumber // 26)))
            res.append(chr(start + (columnNumber % 26)))
            
            columnNumber = columnNumber // 26

        return ''.join(res)