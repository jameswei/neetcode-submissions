class Solution:
    def simplifyPath(self, path: str) -> str:
        # '/neetcode/practice//...///../courses'
        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        separated = path.split("/")
        stack = []

        EMPTY = ""
        SINGLE_PERIOD = "."
        DOUBLE_PERIOD = ".."

        for part in separated:
            if part == EMPTY:
                continue
            
            # valid directory or file
            if part != SINGLE_PERIOD and part != DOUBLE_PERIOD:
                stack.append(part)

            elif part == SINGLE_PERIOD:
                continue

            elif part == DOUBLE_PERIOD:
                if len(stack) > 0:
                    stack.pop()


        return "/"+"/".join(stack)