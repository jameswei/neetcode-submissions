# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # 注意，只删除 val==target 的**叶子**节点

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            marked = node.val == target

            left_child = dfs(node.left)
            right_child = dfs(node.right)

            if marked and not left_child and not right_child:
                return None

            # 要么val!=target，要么val==target但它不是叶子节点
            else:
                node.left = left_child
                node.right = right_child
                return node

        
        return dfs(root)