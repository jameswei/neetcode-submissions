class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return heights[0] * heights[1]
        
        n = len(heights)
        max_area = 0

        left, right = 0, n - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(max_area, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area