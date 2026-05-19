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
        
        return self.check_bst(root.left, [-1000, root.val]) and self.check_bst(root.right, [root.val, 1000])
        

    def check_bst(self, root: Optional[TreeNode], val_range: List[int]) -> bool:
        if root is None:
            return True
        min_val, max_val = val_range[0], val_range[1]
        if root.val < min_val or root.val > max_val:
            return False
        
        return self.check_bst(root.left, [min_val, root.val]) and self.check_bst(root.right, [root.val, max_val])
