class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        deduplicated = set()
        for num in nums:
            deduplicated.add(num)
        
        length = 1
        longest = 1

        # [2,20,4,10,3,4,5]
        # {2,20,4,10,3,5}
        for num in nums:
            prev = num - 1
            if prev in deduplicated:
                continue
            else:
                cur = num + 1
                while cur in deduplicated:
                    length +=1
                    longest = max(longest, length)
                    cur += 1
                length = 1
        
        return longest