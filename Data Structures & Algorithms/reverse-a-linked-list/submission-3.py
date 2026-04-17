# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = self.traverse(head)
        return new_head

    
    def traverse(self, cur_node: ListNode) -> ListNode:
        next_node =cur_node.next
        if next_node is None:
            return cur_node

        new_head = self.traverse(next_node)
        cur_node.next = None
        next_node.next = cur_node
        return new_head
