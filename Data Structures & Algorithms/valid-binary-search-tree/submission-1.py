# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # single node
        if root.left is None and root.right is None:
            return True
        left_is_valid, right_is_valid = True, True
        if root.left is not None:
            left_is_valid = self.isValidBST(root.left) and root.val > root.left.val
        if root.right is not None:
            right_is_valid = self.isValidBST(root.right) and root.val < root.right.val
        
        return left_is_valid and right_is_valid
            