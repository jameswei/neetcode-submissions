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
            anchor_val = nums[i]
            # if anchor_val in memo:
            #     # skip
            #     continue
            difference = 0 - anchor_val
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
                    result.append([anchor_val, nums[j], nums[k]])
                    break
            # put anchor_val into memo
            # memo.add(anchor_val)
        return result