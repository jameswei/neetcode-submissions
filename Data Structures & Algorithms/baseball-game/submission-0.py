class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add, clear, double = "+", "C", "D"

        for op in operations:
            if op == add:
                num_1 = int(stack.pop())
                num_2 = int(stack.pop())
                res = num_1+num_2
                stack.extend([str(num_1), str(num_2), str(res)])
            elif op == clear:
                stack.pop()
            elif op == double:
                num_1 = int(stack.pop())
                res = num_1*2
                stack.extend([str(num_1), str(res)])
            else:
                # 数字
                stack.append(op)

        total_sum = 0
        while len(stack) > 0:
            total_sum += int(stack.pop())

        return total_sum