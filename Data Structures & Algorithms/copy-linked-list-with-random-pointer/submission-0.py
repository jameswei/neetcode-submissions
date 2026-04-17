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
        if not head:
            return None

        orig_to_cloned = {}

        prev, cur = None, head

        while cur is not None:
            
            # 当前节点没被 clone 过
            if cur not in orig_to_cloned:
                orig_to_cloned[cur] = Node(cur.val)
            
            # 有前序节点，就需要连接前序节点和当前节点
            if prev is not None:
                # 前序节点肯定被clone过
                orig_to_cloned[prev].next = orig_to_cloned[cur]

            # 有 random 后续节点
            if cur.random is not None:
                # random 后续节点没被 clone 过
                if cur.random not in orig_to_cloned:
                    orig_to_cloned[cur.random] = Node(cur.random.val)

                # 提前连接当前节点和后续节点
                orig_to_cloned[cur].random = orig_to_cloned[cur.random]
            
            # 沿着 next 遍历链表
            prev = cur
            cur = cur.next

        # cur is None, traversal done
        return orig_to_cloned[head]