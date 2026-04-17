class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        i, j = 0, len(nums)-1

        while i <= j:
            mid = i+(j-i)//2
            pivot = nums[mid]
            if target < pivot:
                j = mid-1
            elif target > pivot:
                i = mid+1
            else:
                return mid
        
        return -1
