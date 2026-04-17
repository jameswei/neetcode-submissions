class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 题目要求的O(1)空间，可以使用快慢指针找链表是否有环的方式
        # 把nums的索引i 以及该索引对应的数值nums[i]分别看成链表的值和指针

        slow, fast = 0, 0

        while True:
            # slow moves 1 step per round
            slow = nums[slow]

            # fast moves 2 steps per round
            fast = nums[fast]
            fast = nums[fast]

            # slow meets fast
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

        return 0
