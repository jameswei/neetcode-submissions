class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        num_to_count = {}
        for num in nums:
            count = num_to_count.get(num, 0) + 1
            num_to_count[num] = count

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in num_to_count.items():
            buckets[count].append(num)
        
        top_k = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
        return top_k