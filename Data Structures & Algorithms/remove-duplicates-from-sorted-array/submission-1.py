class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i, j, n = 0, 0, len(nums)
        prev = 2**31-1
        while j < n:
            cur = nums[j]
            if cur != prev:

                if i != j:
                    nums[i] = cur

                i += 1
                j += 1
            
            # 找到重复元素
            else:
                j += 1

            prev = cur

        return i