# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0

        # [1,2,3,4,5]=>[3,2,1,4,5]
        while cur is not None and count < k:
            cur = cur.next
            count += 1

        if count == k:
            new_head = self.reverseKGroup(cur, k)
            while count > 0:
                temp = head.next
                head.next = new_head
                new_head = head
                head = temp
                count -= 1
            head = new_head
        
        return head