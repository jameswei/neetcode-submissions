class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        # 这题目要求解是k个元素的subarray，所以对于定长窗口，可以进一步简化滑动窗口的实现方式
        # 直接计算第一个窗口的距离和，也就是[0,k)
        dist_sum_in_window = 0

        for i in range(k):
            dist_sum_in_window += abs(arr[i] - x)

        # 直接以第一个窗口的结果作为min_distance的初始值，按照规则，本质是找比它小的解
        min_dist_sum = dist_sum_in_window
        i, j = 0, k
        res = arr[i:j]
        while j < n:
            # 因为定长，可以同时扩大窗口和缩小窗口
            j += 1
            i += 1
            new_dist, old_dist = abs(arr[j-1] - x), abs(arr[i-1] - x)
            dist_sum_in_window += new_dist
            dist_sum_in_window -= old_dist

            if dist_sum_in_window < min_dist_sum:
                min_dist_sum = dist_sum_in_window
                res = arr[i:j]

        return res