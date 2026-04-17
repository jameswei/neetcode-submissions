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
            is_same = self.isSameTree(root, subRoot)
            if is_same:
                return True

            is_left_same = self.isSubtree(root.left, subRoot)
            if is_left_same:
                return True

            is_right_same = self.isSubtree(root.right, subRoot)
            return is_right_same

        else:
            is_left_same = self.isSubtree(root.left, subRoot)
            if is_left_same:
                return True

            is_right_same = self.isSubtree(root.right, subRoot)
            return is_right_same


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False
        
        p_val, q_val = p.val, q.val
        if p_val != q_val:
            return False
        is_left_same = self.isSameTree(p.left, q.left)
        if not is_left_same:
            return False
        is_right_same = self.isSameTree(p.right, q.right)
        if not is_right_same:
            return False
        
        return True







