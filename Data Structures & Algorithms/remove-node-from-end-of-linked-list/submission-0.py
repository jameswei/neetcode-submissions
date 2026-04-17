# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast, prev = dummy, dummy, dummy
        while fast.next is not None:
            fast = fast.next
            n -= 1
            if n <= 0:
                slow = slow.next
            if n < 0:
                prev = prev.next
        
        # slow is at the Nth node counted from tail
        prev.next = slow.next
        return dummy.next