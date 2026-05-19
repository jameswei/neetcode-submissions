# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # root is good node
        num_of_good_nodes = 1

        # 3
        # 3
        # 4 2

        def dfs(node: TreeNode, parent_val: int):
            nonlocal num_of_good_nodes

            if node.val >= parent_val:
                num_of_good_nodes += 1

            if node.left:
                dfs(node.left, node.val)
            if node.right:
                dfs(node.right, node.val)

        dfs(root, root.val)
        return num_of_good_nodes