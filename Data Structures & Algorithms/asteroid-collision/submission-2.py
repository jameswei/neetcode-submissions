class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) > 0:
                # 同符号相乘>0
                if stack[-1] * a > 0 or stack[-1] < 0 and a > 0:
                    stack.append(a)
                else:
                    if abs(stack[-1]) == abs(a):
                        stack.pop()
                    # a < 0 moves to left
                    elif abs(stack[-1]) < abs(a):
                        while len(stack) > 0 and stack[-1] > 0 and abs(stack[-1]) < abs(a):
                            stack.pop()
                        
                        if len(stack) == 0 or stack[-1] < 0:
                            stack.append(a)

            else:
                stack.append(a)
        
        return stack