class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []

        res = []
        for i in range(n-3):
            # 跳过重复数
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 剪枝
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue

            num_1 = nums[i]
            
            for j in range(i+1, n-2):
                # 跳过重复数
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                num_2 = nums[j]

                # 剪枝
                if num_1+num_2+nums[j+1]+nums[j+2] > target:
                    break
                if num_1+num_2+nums[n-1]+nums[n-2] < target:
                    continue

                # 变成 2sum 问题，和是 remaining
                remaining = target-(num_1+num_2)
                l, r = j+1, n-1
                while l < r:
                    num_3, num_4 = nums[l], nums[r]
                    if num_3+num_4 == remaining:
                        res.append([num_1, num_2, num_3, num_4])
                        # 找到解之后，避免出现重复数的新解，跳过重复数
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1 
                        r -= 1
                    elif num_3+num_4 < remaining:
                        l += 1
                    else:
                        r -= 1

        return res