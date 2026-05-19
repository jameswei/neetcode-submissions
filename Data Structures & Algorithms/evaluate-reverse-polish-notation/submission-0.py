class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    val = int(a) + int(b)
                    stack.append(str(val))
                elif t == "-":
                    val = int(b) - int(a)
                    stack.append(str(val))
                elif t == "*":
                    val = int(a) * int(b)
                    stack.append(str(val))
                elif t == "/":
                    val = int(b) // int(a)
                    stack.append(str(val))

        return int(stack[-1])