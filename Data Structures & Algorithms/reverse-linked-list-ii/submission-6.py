# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 题目要求一趟遍历完成，那就不用一下找到left，right范围，先走到left节点
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        # cur指向left节点，prev指向left前一个，如果prev==dummy，说明没有前部
        for _ in range(left-1):
            prev = cur
            cur = cur.next

        print(f"prev: {prev.val}, cur: {cur.val}")
        
        new_tail = cur
        new_head = cur
        
        for _ in range(right-left):
            new_head = new_head.next
        
        nxt = new_head.next

        # 断开连接
        prev.next = None
        new_head.next = None

        # 反转
        i, j = None, new_tail
        while j is not None:
            k = j.next
            j.next = i
            i = j
            j = k

        # 重新连接
        prev.next = i
        new_tail.next = nxt

        return dummy.next