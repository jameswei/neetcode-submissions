class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        first_lower_bar_on_left = [-1] * len(heights)
        first_lower_bar_on_right = [len(heights)] * len(heights)

        for i in range(1, len(heights)):
            j = i-1

            while j >= 0 and heights[j] >= heights[i]:
                j = first_lower_bar_on_left[j]
            
            first_lower_bar_on_left[i] = j
        
        for i in range(len(heights)-2 , -1 ,-1):
            j = i+1

            while j < len(heights) and heights[j] >= heights[i]:
                j = first_lower_bar_on_right[j]
            
            first_lower_bar_on_right[i] = j


        # now we know each bar's left and right boundary
        largest_area = 0
        for i in range(len(heights)):
            h = heights[i]
            w = (first_lower_bar_on_right[i]-1)-(first_lower_bar_on_left[i]+1)+1
            area = h * w
            largest_area = max(largest_area, area)

        return largest_area