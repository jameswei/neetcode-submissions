# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return None

            if node.val == key:
                if node.left and node.right:
                    # 把左子树挂在右子树最左边
                    cur = node.right
                    while cur.left is not None:
                        cur = cur.left
                    cur.left = node.left
                    
                    # 右子树的根作为新的根返回
                    return node.right
                elif node.left:
                    return node.left
                else:
                    return node.right

            if key > node.val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)

            return node

        return dfs(root)
