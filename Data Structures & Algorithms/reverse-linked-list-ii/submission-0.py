# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 0
        new_h, new_t = None, None
        
        cur = head
        while cur is not None:
            count += 1
            if count == left:
                new_t = cur
            # 不能else-if，因为right可能和left相同
            if count == right:
                new_h = cur
                break
            
            cur = cur.next

        cur, nxt = new_t, new_t.next
        while cur != new_h:
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp

        # 接上剩余部分
        new_t.next = nxt

        return new_h