# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 先还原成两个integer
        int1, int2 = 0, 0
        times = 1
        cur = l1
        while cur is not None:
            int1 += cur.val * times
            times *= 10
            cur = cur.next

        times = 1
        cur = l2
        while cur is not None:
            int2 += cur.val * times
            times *= 10
            cur = cur.next

        # 求和
        int3 = int1 + int2

        # 再按位转成链表
        times = 10
        head = ListNode(int3 % times)
        prev = head
        int3 = int3 // times

        while int3 > 0:
            val = int3 % times
            int3 = int3 // times
            
            cur = ListNode(val)
            prev.next = cur
            prev = cur

        return head