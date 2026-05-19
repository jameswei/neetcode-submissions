# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def is_balanced(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_height = is_balanced(node.left)
            right_height = is_balanced(node.right)

            return max(left_height, right_height) + 1

        left_height = is_balanced(root.left)
        right_height = is_balanced(root.right)

        return abs(left_height-right_height) < 2