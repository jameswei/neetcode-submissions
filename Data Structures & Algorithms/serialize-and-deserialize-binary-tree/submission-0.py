# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        node_vals = list()
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                cur = queue.popleft()
                node_vals.append(str(cur.val) if cur is not None else "x")
                if cur is not None:
                    queue.append(cur.left)
                    queue.append(cur.right)

        res =  ",".join(node_vals)
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data is None or len(data) == 0:
            return None
        
        nodes = list()
        node_vals = data.split(",")
        print(node_vals)
        for i in range(len(node_vals)):
            node = TreeNode(int(node_vals[i])) if node_vals[i] != "x" else None
            nodes.append(node)
        
        for i in range(len(nodes)):
            if nodes[i] is None:
                continue
            nodes[i].left = nodes[i*2+1] if i*2+1 < len(nodes) else None
            nodes[i].right = nodes[i*2+2] if i*2+2 < len(nodes) else None

        return nodes[0]
            
