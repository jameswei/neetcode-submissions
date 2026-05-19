class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                if t == "+":
                    val = 0
                    while len(stack) > 0:
                        val += int(stack.pop())
                    stack.append(str(val))
                elif t == "-":
                    operand = []
                    while len(stack) > 0:
                        operand.append(stack.pop())
                    val = int(operand[0])
                    for i in range(1, len(operand)):
                        val -= int(operand[i])
                    stack.append(str(val))
                elif t == "*":
                    val = 1
                    while len(stack) > 0:
                        val *= int(stack.pop())
                    stack.append(str(val))
                elif t == "/":
                    operand = []
                    while len(stack) > 0:
                        operand.append(stack.pop())
                    val = int(operand[0])
                    for i in range(1, len(operand)):
                        val = val // int(operand[i])
                    stack.append(str(val))

        return int(stack[-1])