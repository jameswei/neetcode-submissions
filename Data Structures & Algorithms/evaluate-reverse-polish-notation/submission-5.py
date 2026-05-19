class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if t == "+":
                    val = 0
                    while len(stack) > 0:
                        val += stack.pop()
                    stack.append(val)
                elif t == "-":
                    operand = []
                    while len(stack) > 0:
                        operand.append(stack.pop())
                    val = operand[0]
                    for i in range(1, len(operand)):
                        val -= operand[i]
                    stack.append(val)
                elif t == "*":
                    val = 1
                    while len(stack) > 0:
                        val *= stack.pop()
                    stack.append(val)
                elif t == "/":
                    operand = []
                    while len(stack) > 0:
                        operand.append(stack.pop())
                    val = operand[0]
                    for i in range(1, len(operand)):
                        val = val // operand[i]
                    stack.append(val)

        return int(stack[-1])