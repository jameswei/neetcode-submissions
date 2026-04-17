class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        num_count = defaultdict(int)
        min_num, max_num = 0, 2
        for num in nums:
            num_count[num] += 1

        i = 0
        for j in range(3):
            cnt = num_count[j]

            if cnt > 0:
                for _ in range(cnt):
                    nums[i] = j
                    i += 1

        return

