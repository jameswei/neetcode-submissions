class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 朴素双指针解法，l和r分别在arr[]首尾，然后收缩l和r，直到找到解
        n = len(arr)
        l, r = 0, n-1

        while r-l+1 > k:
            l_dist = abs(arr[l] - x)
            r_dist = abs(arr[r] - x)

            if l_dist < r_dist:
                r -= 1
            elif l_dist > r_dist:
                l += 1
            else:
                # 同距离情况下，r索引>l索引
                r -= 1
        
        # 此时 r-l+1 == k
        return arr[l:r+1]