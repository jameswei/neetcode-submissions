class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
                continue
            
            while len(stack) > 0 and stack[-1] > 0 and a < 0 and abs(stack[-1]) < abs(a):
                stack.pop()

            # 要么stack空了，要么无冲突，
            if len(stack) == 0 or stack[-1]*a > 0 or stack[-1] < 0 and a > 0:
                stack.append(a)
            
            # 要么栈顶更大、或相等
            elif len(stack) > 0 and stack[-1] > 0 and a < 0 and abs(stack[-1]) == abs(a):
                stack.pop()
            
        
        return stack