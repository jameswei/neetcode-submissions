class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = list()
        pair = {'(':')', '{':'}', '[':']'}

        for cur in s:
            if cur in pair.keys():
                stack.append(cur)
            elif cur in pair.values():
                prev = stack.pop()
                if prev != pair[cur]:
                    return False
        return True
