class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # sort
        nums.sort()

        result = list()

        # [0, len-2)
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                # no need
                continue;
            difference = 0 - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum_val = nums[j] + nums[k]
                if sum_val < difference:
                    # move j to right
                    j += 1
                    continue
                elif sum_val > difference:
                    # move k to left
                    k -= 1
                    continue

                # sum_val == difference, get an answer, 
                # but may have duplicated triplet
                result.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
        return result