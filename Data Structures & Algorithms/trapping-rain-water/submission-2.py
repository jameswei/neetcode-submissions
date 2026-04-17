class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
    
        left, right = 0, len(height) - 1
        # 记录左右两侧遇到的最大高度
        left_max, right_max = 0, 0
        total = 0
        
        while left < right:
            # 更新左右两侧的最大高度
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # 关键：移动较矮的一侧
            if height[left] < height[right]:
                # 对于left位置，水量由left_max决定
                total += left_max - height[left]
                left += 1
            else:
                # 对于right位置，水量由right_max决定
                total += right_max - height[right]
                right -= 1
        
        return total