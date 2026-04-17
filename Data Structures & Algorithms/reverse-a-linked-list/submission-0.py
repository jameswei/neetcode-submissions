# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        cur_node, next_node, prev_node = head, head.next, None
        while next_node:
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            next_node = cur_node.next
        cur_node.next = prev_node
        return cur_node