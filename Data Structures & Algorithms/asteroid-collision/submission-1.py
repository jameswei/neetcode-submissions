class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) > 0:
                # 同符号相乘>0
                if stack[-1] * a > 0:
                    stack.append(a)
                else:
                    if abs(stack[-1]) == abs(a):
                        stack.pop()
                    else:
                        while len(stack) > 0 and stack[-1] * a < 0 and abs(stack[-1]) <= abs(a):
                            stack.pop()

            else:
                stack.append(a)
        
        return stack