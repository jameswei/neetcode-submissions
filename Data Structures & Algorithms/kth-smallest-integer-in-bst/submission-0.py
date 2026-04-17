# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # in-order traversal will get an ordered array.
        def in_order_traverse(node: Optional[TreeNode], k: int, res: List[int]):
            if node is None:
                return
            in_order_traverse(node.left, k, res)
            res.append(node.val)
            in_order_traverse(node.right, k, res)

        res = list()
        in_order_traverse(root, k, res)
        return res[k-1]


