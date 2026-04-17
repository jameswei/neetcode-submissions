class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        highest_on_left = [0] * len(height)
        highest_on_left[0] = height[0]

        highest_on_right = [0] * len(height)
        highest_on_right[-1] = height[-1]

        for i in range(1, len(height)):
            highest_on_left[i] = max(height[i], highest_on_left[i-1])

        for i in range(len(height)-2, -1, -1):
            highest_on_right[i] = max(height[i], highest_on_right[i+1])

        total = 0
        
        for i in range(len(height)):
            vol = min(highest_on_left[i], highest_on_right[i]) - height[i]
            if vol > 0:
                total += vol
        
        return total