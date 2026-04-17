class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        # 标准的二分查找解法，l最终就是应该插入target的位置
        # 因为l的移动方式是跳过所有<target的元素
        while l <= r:
            mid = (l+r)//2
            n = nums[mid]

            # 严格区分三种情况，在没找到target时会直接跳过mid
            if n == target:
                return mid
            elif n > target:
                r = mid - 1
            else:
                l = mid + 1

        # 此时l和r交错，l == r+1
        return l