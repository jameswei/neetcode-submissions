# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter 可以这样求：
        # 左子树深度
        # 右子树深度
        # 左子树深度+右子树深度
        # 以上 3 种值都作为 diameter 的备选，通过 max()来更新
        # 用dfs遍历

        diameter = 0

        # 返回深度/高度
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_h = dfs(node.left)
            left_r = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left_h)
            diameter = max(diameter, left_r)
            diameter = max(diameter, left_h+left_r)
            
            return max(left_h, left_r)+1

        dfs(root)
        return diameter
