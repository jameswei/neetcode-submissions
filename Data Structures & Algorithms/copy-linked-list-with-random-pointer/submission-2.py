"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        old_to_new = {}

        # 两遍遍历法
        # 先clone同时处理next关系
        prev, cur = None, head
        while cur is not None:
            old_to_new[cur] = Node(cur.val)
            
            if prev is not None:
                old_to_new[prev].next = old_to_new[cur]

            prev = cur
            cur = cur.next

        # 再处理random关系
        cur = head
        while cur is not None:
            if cur.random is not None:
                old_to_new[cur].random = old_to_new[cur.random]

            cur = cur.next

        return old_to_new[head]
        