class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        # a monotonical decreasing queue
        queue = deque()

        for i in range(n):
            num = nums[i]
            # push num into queue,
            while len(queue) > 0 and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)

            # j-i+1==k
            if len(queue) > 0 and queue[0] < i-k+1:
                queue.popleft()

            # i-0+1==k
            if i >= k-1:
                res.append(nums[queue[0]])
            
        return res

            


