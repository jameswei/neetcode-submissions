# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        if len(inorder) == 1:
            # return a single node
            return TreeNode(preorder[0])
        
        root_val = preorder[0]

        root_idx = -1
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                root_idx = i
                break
        root = TreeNode(root_val)

        # inorder[0:root_id] on the left side
        left_inorder = inorder[0:root_idx]
        left_len = len(left_inorder)
        left_preorder = preorder[1:1+left_len]
        root.left = self.buildTree(left_preorder, left_inorder)

        # inorder[root_id+1:] on the right side
        right_inorder = inorder[root_idx+1:]
        right_len = len(right_inorder)
        right_preorder = preorder[1+left_len:]
        root.right = self.buildTree(right_preorder, right_inorder)

        return root



