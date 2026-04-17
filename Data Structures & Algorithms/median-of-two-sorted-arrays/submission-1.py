class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 and nums2 are sorted
        # no need to fully merge them together

        len1, len2 = len(nums1), len(nums2)

        # 因为两个数组已经是有序的，可以用类似“归并排序”的方式，但不用真的排序
        total = len1 + len2
        i, j = 0, 0
        mid = total//2
        # 比较两个指针对应的数值，每次取较小的值，放入新数组
        # 因为总长度已知，所以当取到(m+n)/2时，就是median num中位数
        
        cur, prev = 0, 0

        for k in range(mid+1):
            prev = cur
            
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    cur = nums1[i]
                    i += 1
                else:
                    cur = nums2[j]
                    j += 1
            elif i < len1:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
        
        if total % 2 == 0:
            return (prev+cur) / 2.0
        else:
            return float(cur)