class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [0] * (m+n)

        i, j, k = 0, 0, 0

        while k < len(res):
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    res[k] = nums1[i]
                    i += 1
                else:
                    res[k] = nums2[j]
                    j += 1
            elif i < m:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1

            k += 1

        for idx in range(len(res)):
            nums1[idx] = res[idx]
