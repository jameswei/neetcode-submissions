class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_count = len(nums)//3

        # 需要先排序
        nums.sort()

        res = []
        prev_num = nums[0]
        occurrence = 1
        print(f"nums: {nums}")

        for i in range(1, len(nums)):
            if nums[i] == prev_num:
                occurrence += 1
            else:
                if occurrence > min_count:
                    res.append(prev_num)
                
                prev_num = nums[i]
                occurrence = 1

        if occurrence > min_count:
            res.append(prev_num)
            
        return res

