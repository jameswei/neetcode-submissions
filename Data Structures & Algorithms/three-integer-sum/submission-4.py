class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # sort
        nums.sort()

        result = list()
        n = len(nums)

        for i in range(0, n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]
                if sum_val == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum_val < 0:
                    j += 1
                else:
                    k -= 1
        
        return result