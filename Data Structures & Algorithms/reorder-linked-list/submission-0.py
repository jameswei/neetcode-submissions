# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        slow, fast = head, head
        while fast is not None:
            if fast.next is not None:
                fast = fast.next.next
            else:
                break
            slow = slow.next

        # now slow is at mid position
        # reverse the second part
        prev_node, cur_node = None, slow.next
        slow.next = None
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        # now prev_node is the reversed list's head node, 
        # which is the tail node of the original list

        # head and prev_node are the head nodes of two parts
        # merge two parts
        h1, h2 = head, prev_node
        while h2 is not None:
            next_node = h1.next
            h1.next = h2
            h1 = next_node
            next_node = h2.next
            h2.next = h1
            h2 = next_node

        return