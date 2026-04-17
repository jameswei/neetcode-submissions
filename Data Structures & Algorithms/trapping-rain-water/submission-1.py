class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        # mono stack
        stack = list()
        total = 0

        for i in range(len(height)):
            if len(stack) == 0:
                stack.append(i)
                continue

            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and height[i] > height[stack[-1]]:
                    mid = stack.pop()
                    if len(stack) > 0:
                        left = stack[-1]
                        vol = (min(height[left], height[i])-height[mid]) * (i-left-1)
                        if vol > 0:
                            total += vol

                stack.append(i)        
        
        return total