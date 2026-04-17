# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        right_view_nodes = []

        # 既然要求是“每一层最右边的节点”，那 bfs 按层遍历是最自然的解法
        # 而“最右的节点”在 bfs 遍历过程中就是每一层最后一个节点
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            nodes_in_current_level = len(queue)
            # 每一层最多 2^i 个节点，单只选择最后一个节点，就是“最右的节点”
            for i in range(nodes_in_current_level):
                cur = queue.popleft()
                if cur and cur.left:
                    queue.append(cur.left)
                if cur and cur.right:
                    queue.append(cur.right)
                
                if cur and i == (nodes_in_current_level-1):
                    right_view_nodes.append(cur.val)

        return right_view_nodes