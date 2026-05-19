class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        b, e = 0, n-1

        while b < e:
            mid = (b+e)//2
            n = nums[mid]
            if n == target:
                return mid
            elif n < target:
                b = mid + 1
            else:
                e = mid - 1

        return b+1