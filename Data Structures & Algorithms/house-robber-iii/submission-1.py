# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # 记忆表，某节点为根的子树在约束下的最大收益
        memo = {}
        
        # 记忆化+dfs 
        def dfs(node: Optional[TreeNode], parent_robbed: bool) -> int:
            if node is None:
                return 0
            
            if (node, parent_robbed) in memo:
                return memo[(node, parent_robbed)]
            
            cur_amount = 0

            # 既可以选也可以不选，返回最大收益
            if not parent_robbed:
                cur_amount = max(cur_amount, dfs(node.left, True)+dfs(node.right, True)+node.val)
                cur_amount = max(cur_amount, dfs(node.left, False)+dfs(node.right, False))
            
            # 不能选，只能返回当前约束下的收益
            else:
                cur_amount = dfs(node.left, False)+dfs(node.right, False)

            memo[(node, parent_robbed)] = cur_amount
            return cur_amount

        return dfs(root, False)