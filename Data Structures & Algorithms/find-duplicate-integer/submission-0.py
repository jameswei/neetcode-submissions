class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 要求不改变 nums，说明不能原地排序
        # 又要求O(1)空间，说明也不能排序到新数组

        # 是用bitmask的话，所有数组都位于[1,n]区间，-1可以映射到[0,n-1]个比特位
        bit_slot = 0b0
        mask = 0b1

        for i in range(len(nums)):
            num = nums[i]
            bit_pos = mask << (num-1)
            if bit_slot & bit_pos:
                return num
            
            bit_slot = bit_slot | bit_pos

        return 0
