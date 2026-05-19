# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # dfs是遍历的方式，但是更新结果不是在一条路径结束后产生，而是要全部遍历完
        # parent_selected就是每层递归时的约束，可以决定继续递归的可能路径
        def dfs(node: Optional[TreeNode], parent_selected: bool) -> int:
            if node is None:
                return 0

            cur_amount = 0
            
            # 既可以选也可以不选
            if not parent_selected:
                cur_amount = max(cur_amount, dfs(node.left, True)+dfs(node.right, True)+node.val)
                cur_amount = max(cur_amount, dfs(node.left, False)+dfs(node.right, False))
                return cur_amount
            
            # 只能不选
            else:
                cur_amount = dfs(node.left, False)+dfs(node.right, False)

            return cur_amount

        return dfs(root, False)