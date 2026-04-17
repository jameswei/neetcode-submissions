class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 根据题目要求，需要在给定“范围”内寻找满足条件的情况，
        # 所以一个定长为k的sliding window解法更合适
        n = len(nums)
        # 左闭右开, size==j-i
        i, j = 0, 0
        size = k+1

        nums_in_window = set()

        while i < n and j <= n:
            # 增长窗口到定长k
            while j < n and j-i < size:
                j += 1
                new_n = nums[j-1]
                if new_n in nums_in_window:
                    return True
                
                nums_in_window.add(new_n)

            # j==n or j-i==k+1
            
            # 缩小窗口
            old_n = nums[i]
            nums_in_window.remove(old_n)
            i += 1

        return False
        