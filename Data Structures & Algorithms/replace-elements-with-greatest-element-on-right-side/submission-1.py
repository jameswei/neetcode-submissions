class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        largest_to_right = -1

        for i in range(n-1, -1, -1):
            res[i] = largest_to_right
            largest_to_right = max(largest_to_right, arr[i])

        return res