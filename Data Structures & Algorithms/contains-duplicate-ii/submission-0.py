class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 要求数相等，但是距离小于等于k，所以不能排序，否则会破坏原有顺序
        # 暴力解，从左向右遍历每个num，再遍历它向右至多k个num，检查是否相等

        n = len(nums)

        for i in range(n):
            num_1 = nums[i]

            for j in range(i+1, i+k+1):
                if j > n-1:
                    continue

                num_2 = nums[j]

                if num_1 == num_2:
                    return True

        return False