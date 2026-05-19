# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is None:
            return False
        
        if root.val == subRoot.val:
            is_left_same = self.isSubtree(root.left, subRoot.left)
            is_right_same = self.isSubtree(root.right, subRoot.right)
            if is_left_same and is_right_same:
                return True
            return False
        else:
            is_left_same = self.isSubtree(root.left, subRoot)
            if not is_left_same:
                is_right_same = self.isSubtree(root.right, subRoot)
                return is_right_same
            return True









