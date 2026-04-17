class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        m = 0
        l, r = 1, n-2
        while l<=r:
            m = (l+r)//2
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if  left<mid<right:
                l = m+1
            elif left>mid>right:
                r = m-1
            else:
                break
        # 因为不满足单调性，m是可能的高峰，也就是分界点
        peak = m 

        # 分别搜索两侧
        l, r = 0, peak-1
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:
                r = m-1
            else:
                l = m+1

        l, r = peak, n-1
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val == target:
                return m
            # 不等的情况下要反过来收缩方向，因为右侧是递减
            elif val < target:
                r = m-1
            else:
                l = m+1

        return -1
