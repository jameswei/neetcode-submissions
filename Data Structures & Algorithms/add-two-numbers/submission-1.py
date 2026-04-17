# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2

        times = 10
        carry = 0
        prev, head = None, None

        while h1 is not None and h2 is not None:
            v1, v2 = h1.val, h2.val
            v3 = v1 + v2 + carry

            carry = v3 // times
            node = ListNode(v3 % times)

            if prev is None:
                head = node

            if prev is not None:
                prev.next = node
            prev = node

            h1 = h1.next
            h2 = h2.next

        # either h1 is None or h2 is None
        while h1 is not None:
            val = h1.val + carry
            
            carry = val // times
            node = ListNode(val % times)

            prev.next = node
            prev = node

            h1 = h1.next

        while h2 is not None:
            val = h2.val + carry
            
            carry = val // times
            node = ListNode(val % times)

            prev.next = node
            prev = node

            h2 = h2.next

        if carry > 0:
            node = ListNode(carry)
            prev.next = node
            prev = node

        return head