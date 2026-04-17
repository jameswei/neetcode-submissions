class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        num_to_count = {}
        
        # counting
        for cur_num in nums:
            cnt = num_to_count.get(cur_num, 0) + 1
            num_to_count[cur_num] = cnt

        # select top-k
        items = num_to_count.items()
        top_k = heapq.nlargest(k, items, key=lambda kv: kv[1])
        result = []
        for k, _ in top_k:
            result.append(k)
        return result