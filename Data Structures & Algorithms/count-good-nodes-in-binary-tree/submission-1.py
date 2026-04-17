# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # root is good node
        num_of_good_nodes = 0

        # 3
        # 3
        # 4 2

        def dfs(node: TreeNode, max_val_on_path: int):
            nonlocal num_of_good_nodes

            if node.val >= max_val_on_path:
                num_of_good_nodes += 1

            if node.left:
                dfs(node.left, max(node.val, max_val_on_path))
            if node.right:
                dfs(node.right, max(node.val, max_val_on_path))

        dfs(root, root.val)
        return num_of_good_nodes