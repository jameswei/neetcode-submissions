class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # nums发生了rotate，但不知道rotation的次数
        # rotation的次数按照len取模，取值范围是[0,len-1]，如果==0，等同于没有rotate
        # 所以要区分rotation在左侧还是右侧的情况，这影响了二分查找缩小范围的方向

        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            m = l+(r-l)//2

            if nums[m] == target:
                return True

            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            # 右侧
            elif nums[m] <= nums[r]:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
            
            # 左侧
            elif nums[m] >= nums[l]:
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1


        return False