class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        cur_largest = arr[n-1]
        arr[n-1] = -1

        for i in range(n-2, -1, -1):
            tmp = arr[i]
            arr[i] = cur_largest
            cur_largest = max(cur_largest, tmp)

        return arr
