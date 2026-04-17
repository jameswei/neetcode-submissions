# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        cur_node, prev_node = head, None
        while cur_node:
            tmp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = tmp
            
        return prev_node