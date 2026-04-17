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
            # valid directory or file
            if part != SINGLE_PERIOD and part != DOUBLE_PERIOD and part != EMPTY:
                stack.append(part)

            elif part == DOUBLE_PERIOD and len(stack) > 0:
                stack.pop()

        return "/"+"/".join(stack)