class Solution:
    def jump(self, nums: List[int]) -> int:
        # 朴素思路
        # 每一次跳跃时，都跳最大距离，这样总体就离目标更近。
        # 但这样有可能遇到后续都是1格1格的情况，使得最终步数不是最优
        # 正确的贪心思路
        # 每一次跳跃前，看看能跳的范围内[1,最大距离],哪一个落掉接下来能跳更远
        # 这才是最佳选择

        if len(nums) == 1:
            return 0

        i = 0
        jump = 0
        while i < len(nums):
            max_len = nums[i]
            # 从这能直接跳到终点
            if i + max_len >= len(nums) - 1:
                return jump + 1

            if max_len == 1:
                i = i + max_len
            elif max_len > 1:
                next_max_len = 1
                next_i = i + 1
                for j in range(i+1,i+max_len+1):
                    if nums[j] >= next_max_len:
                        next_max_len = nums[j]
                        next_i = j
                i = next_i
            
            jump += 1
        
        return jump