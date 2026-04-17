class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # sort
        nums.sort()
        memo = set()
        result = list()

        # [0, len-2)
        for i in range(0, len(nums) - 2):
            difference = 0 - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum_val = nums[j] + nums[k]
                if sum_val < difference:
                    # move j to right
                    j += 1
                elif sum_val > difference:
                    # move k to left
                    k -= 1
                else:
                    # get an answer, may have duplicated triplet
                    # should break to avoid select duplicated value
                    res = [nums[i], nums[j], nums[k]]
                    tmp = ".".join(str(val) for val in res)
                    if tmp not in memo:
                        result.append(res)
                        memo.add(tmp)
                    j += 1
                    k -= 1
        return result