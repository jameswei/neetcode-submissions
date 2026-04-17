class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        deduplicated = set()
        for num in nums:
            deduplicated.add(num)
        
        longest = 1

        # [2,20,4,10,3,4,5]
        # {2,20,4,10,3,5}
        for num in deduplicated:
            if num - 1 not in deduplicated:
                cur = num + 1
                length = 1
                while cur in deduplicated:
                    cur += 1
                    length +=1
                longest = max(longest, length)           
        
        return longest