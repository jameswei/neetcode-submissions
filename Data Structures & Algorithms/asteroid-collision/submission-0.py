class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) > 0:
                p_a = stack.pop()
                if (p_a > 0 and a > 0) or (p_a < 0 and a < 0):
                    stack.append(p_a)
                    stack.append(a)
                else:
                    if abs(p_a) == abs(a):
                        continue
                    else:
                        stack.append(a if abs(a) > abs(p_a) else p_a)
            else:
                stack.append(a)
        
        return stack