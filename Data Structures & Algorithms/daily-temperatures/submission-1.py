class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        res = [0] * len(temperatures)

        # 维护一个单调减的栈，栈里是temperatures的索引
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]

            if len(stack) > 0 and t > temperatures[stack[-1]]:
                while len(stack) > 0 and t > temperatures[stack[-1]]:
                    j = stack.pop()
                    res[j] = i - j
            
            stack.append(i)

        return res