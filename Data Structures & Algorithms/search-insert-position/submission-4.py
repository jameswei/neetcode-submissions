class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        b, e = 0, n

        # 这是二分查找的lower bound实现方式
        # 目的是找到大于等于target中的最小索引
        while b < e:
            mid = b+(e-b)//2
            n = nums[mid]
            if n >= target:
                e = mid
            else:
                b = mid + 1

        # 此时b和e指向相同元素 b == e
        return b