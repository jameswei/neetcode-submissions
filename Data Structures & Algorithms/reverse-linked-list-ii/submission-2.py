# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        # 反转部分的头和尾，left前和right后
        new_head, new_tail, before, after = None, None, None, None
        
        # cur指向第count个节点
        prev, cur = None, head
        
        # 保证cur始终指向节点，prev在cur之前
        while cur is not None:
            if count == left:
                new_tail = cur
                before = prev
            # 不能else-if，因为right可能和left相同
            if count == right:
                new_head = cur
                after = cur.next
                break
            
            cur = cur.next
            prev = cur
            count += 1

        # 遍历完得到
        # before->new_tail->a->b->c->new_head->after

        prev, cur, nxt = new_tail, new_tail.next, None
        # 反转cur的指向
        while prev != new_head:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 连接原来的部分
        if before is not None:
            before.next = new_head
        new_tail.next = after

        return head if before is not None else new_head