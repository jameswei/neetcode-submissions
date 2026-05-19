class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return 0

        # a monotonical stack
        stack = []

        largest_area = 0

        for i in range(len(heights)):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                continue
            
            height = heights[i]
            width = (i - stack.pop() + 1)*1
            area = height * width
            largest_area = max(largest_area, area)
        
        return largest_area