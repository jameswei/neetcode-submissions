class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr已经是单调递增
        n = len(arr)
        distance_in_window = 0
        index_sum_in_window = 0
        res = []

        min_distance = float('inf')

        i, j = 0, 0

        while j < n:
            j += 1
            distance_in_window += abs(arr[j-1] - x)
            index_sum_in_window += (j - 1)

            if j-i == k:
                if distance_in_window < min_distance:
                    min_distance = distance_in_window
                    res = arr[i:j]
                
            while j-i > k:
                distance_in_window -= abs(arr[i] - x)
                index_sum_in_window -= (i)
                i += 1

                if j-i == k:
                    if distance_in_window < min_distance:
                        min_distance = distance_in_window
                        res = arr[i:j]

        return res