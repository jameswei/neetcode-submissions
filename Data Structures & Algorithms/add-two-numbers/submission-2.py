# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2

        times = 10
        carry = 0
        prev, head = None, None
        
        # 不还原 integer，直接遍历两个链表，相当于从低位开始一位一位做加法
        while h1 is not None and h2 is not None:
            v1, v2 = h1.val, h2.val
            
            # 需要考虑进位的情况，如果前一位产生进位，要加到当前计算中
            v3 = v1 + v2 + carry
            # 同时继续更新进位
            carry = v3 // times
            node = ListNode(v3 % times)

            if prev is None:
                head = node

            if prev is not None:
                prev.next = node
            prev = node

            h1 = h1.next
            h2 = h2.next

        # 如果单个链表遍历结束了，说明没有高位，直接将剩余高位clone一遍
        if h1 is None or h2 is None:
            h = h1 if h1 is not None else h2
            
            while h is not None:
                val = h.val + carry
            
                carry = val // times
                node = ListNode(val % times)

                prev.next = node
                prev = node

                h = h.next    

        # 如果都结束了，说明按位加法结束了，如果有进位，就补一个节点
        if carry > 0:
            node = ListNode(carry)
            prev.next = node
            prev = node

        return head