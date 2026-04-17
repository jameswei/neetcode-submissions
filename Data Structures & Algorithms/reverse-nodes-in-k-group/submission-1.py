# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reversed_head = None

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None

            # [1,2,3,4,5]=>[3,2,1,4,5]
            count = 0
            prev, cur = None, head
            while cur is not None and count < k:
                prev = cur
                cur = cur.next
                count += 1

            if count < k:
                # no reverse and no recursion
                return head
            else:
                # prev is new head
                new_head = prev
                new_tail = head

                # cur is next recursion head
                head_of_remains = reverse(cur)
                
                # reverse [head...prev]
                while count > 0:
                    temp = new_tail.next
                    new_tail.next = head_of_remains
                    head_of_remains = new_tail
                    new_tail = temp
                    count -= 1

                return new_head




        reversed_head = reverse(head)

        return reversed_head