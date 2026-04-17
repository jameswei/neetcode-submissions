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

        def is_balanced(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return (True, 0)

            left_balanced, left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)

            return (left_balanced and right_balanced and abs(left_height-right_height) < 2, max(left_height, right_height) + 1)

        left_balanced, left_height = is_balanced(root.left)
        right_balanced, right_height = is_balanced(root.right)

        return left_balanced and right_balanced and abs(left_height-right_height) < 2 