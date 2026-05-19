class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []

        for t in tokens:
            print(f"token: {t}, stack: {stack}")
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
                    val = operand[len(operand)-1]
                    for i in range(len(operand)-2, -1, -1):
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
                    val = operand[len(operand)-1]
                    for i in range(len(operand)-2, -1, -1):
                        val = val // operand[i]
                    stack.append(val)

        return int(stack[-1])