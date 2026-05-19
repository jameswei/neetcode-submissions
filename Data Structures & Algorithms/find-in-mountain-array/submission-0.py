class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        for i in range(n):
            if mountainArr.get(i) == target:
                return i
        
        return -1