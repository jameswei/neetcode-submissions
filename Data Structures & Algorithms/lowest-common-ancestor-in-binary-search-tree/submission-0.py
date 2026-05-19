# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        val = root.val
        if val == p.val or val == q.val:
            # p or q is the child node
            return root
        elif p.val < val and q.val < val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val < val and q.val > val:
            left = self.lowestCommonAncestor(root.left, p, None)
            right = self.lowestCommonAncestor(root.right, None, q)
            if left is not None and right is not None:
                return root
            else:
                return left if left is not None else right
        elif p.val > val and q.val < val:
            left = self.lowestCommonAncestor(root.right, p, None)
            right = self.lowestCommonAncestor(root.left, None, q)
            if left is not None and right is not None:
                return root
            else:
                return left if left is not None else right


