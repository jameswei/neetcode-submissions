class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add, clear, double = "+", "C", "D"

        for op in operations:
            if op == add:
                num_1 = stack.pop()
                num_2 = stack.pop()
                res = num_1+num_2
                stack.extend([num_2, num_1, res])
            elif op == clear:
                stack.pop()
            elif op == double:
                num_1 = stack.pop()
                res = num_1*2
                stack.extend([num_1, res])
            else:
                # 数字
                stack.append(int(op))

            print(f"stack: {stack}")

        total_sum = 0
        while len(stack) > 0:
            total_sum += stack.pop()

        return total_sum