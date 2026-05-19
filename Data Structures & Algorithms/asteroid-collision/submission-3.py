class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) > 0:
                # 同符号相乘>0
                if stack[-1] * a > 0 or stack[-1] < 0 and a > 0:
                    stack.append(a)
                else:
                    # 完全抵消
                    if abs(stack[-1]) == abs(a):
                        stack.pop()
                    else:
                        # 把所有正数且绝对值小于a的都弹出
                        while len(stack) > 0 and stack[-1] > 0 and abs(stack[-1]) < abs(a):
                            stack.pop()
                        
                        if len(stack) == 0 or stack[-1] < 0:
                            stack.append(a)

            else:
                stack.append(a)
        
        return stack