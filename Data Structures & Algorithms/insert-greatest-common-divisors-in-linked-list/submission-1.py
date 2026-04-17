# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 每两个node，先求gcd，再插入
        # gcd求法：欧几里得辗转相除法

        prev, cur = None, head

        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        while cur is not None:
            if prev is not None:
                # 算gcd
                val = gcd(prev.val, cur.val)
                # 加新node
                gcd_node = ListNode(val)
                prev.next = gcd_node
                gcd_node.next = cur

            prev = cur
            cur = cur.next

        # 如果只有一个node，什么也不做，直接返回head
        return head