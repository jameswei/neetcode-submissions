class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = len(nums)
        expected_sum = expected*(expected+1)//2

        actual_sum = 0
        for n in nums:
            actual_sum += n
        
        missing_num = expected_sum - actual_sum

        return missing_num
