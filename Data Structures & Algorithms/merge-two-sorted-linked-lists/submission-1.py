# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2

        if list1.val <= list2.val:
            if list1.next is not None:
                node = self.mergeTwoLists(list1.next, list2)
                list1.next = node
                return list1
            else:
                list1.next = list2
                return list1
        else:
            # list1.val > list2.val
            if list2.next is not None:
                node = self.mergeTwoLists(list1, list2.next)
                list2.next = node
                return list2
            else:
                list2.next = list1
                return list2
        
