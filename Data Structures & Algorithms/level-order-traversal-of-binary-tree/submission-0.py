# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = list()

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            nodes_in_current_level = list()
            count = len(queue)
            for i in range(0, count):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                nodes_in_current_level.append(node.val)
            result.append(nodes_in_current_level)
        
        return result