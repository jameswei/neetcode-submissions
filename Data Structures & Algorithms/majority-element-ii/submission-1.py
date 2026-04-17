class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        min_count = n // 3
        # O(n)
        num_count = defaultdict(int)

        res = []
        for num in nums:
            num_count[num] += 1

            if num_count[num] == min_count+1:
                res.append(num)

        return res

