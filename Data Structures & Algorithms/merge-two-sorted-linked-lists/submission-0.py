# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        
        p1, p2, dummy = list1, list2, ListNode()
        head = dummy

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                dummy.next = p1
                temp = p1.next
                p1.next = None
                p1 = temp
            else:
                dummy.next = p2
                temp = p2.next
                p2.next = None
                p2 = temp
                
            dummy = dummy.next

        if p1 is not None:
            dummy.next = p1
        else:
            dummy.next = p2
        
        return head.next

            

