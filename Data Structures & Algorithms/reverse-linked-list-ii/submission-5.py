# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 这个解法是先找到边界，从原链表断开，原地反转，再连接回去

        dummy = ListNode(0, head)
        count = 1
        # 反转部分的头和尾，left前和right后
        new_head, new_tail, before, after = None, None, None, None
        
        # cur指向第count个节点
        prev, cur = dummy, head
        
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
            
            prev = cur
            cur = cur.next
            count += 1

        # before->new_tail->a->b->c->new_head->after

        # before和after都有可能是空，如果有的话，那先从原链表中断开
        if before is not None:
            before.next = None
        
        if after is not None:
            new_head.next = None

        # 原地反转链表就是标准的三指针解法
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

        # 这种写法容易遗漏，更好的做法是建一个dummy节点连接head，
        # return head if before is not None else new_head
        # 不管是否有before部分，都直接返回dummy.next
        return dummy.next
        