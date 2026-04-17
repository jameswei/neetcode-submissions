class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        merged.extend(nums1)
        merged.extend(nums2)

        merged.sort()

        if len(merged) % 2 == 0:
            mid = len(merged) // 2
            return (merged[mid-1]+merged[mid])/2.0
        else:
            return merged[len(merged)//2]