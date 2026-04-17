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

                # 这一步使得普通二叉树的空节点没法再挂空的子节点，这会在反序列化时造成下标错乱
                # 也就是说空节点可以有占位符，但是它没法再用占位符填充它的子节点
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
        
        node_vals = data.split(",")
        root = TreeNode(int(node_vals[0]))
        print(node_vals)

        queue = deque()
        queue.append(root)

        i = 1
        while i < len(node_vals):
            parent_node = queue.popleft()
            
            left_val = node_vals[i]
            if left_val != "x":
                left_node = TreeNode(int(left_val))
                parent_node.left = left_node
                queue.append(left_node)
            
            right_val = node_vals[i+1]
            if right_val != "x":
                right_node = TreeNode(int(right_val))
                parent_node.right = right_node
                queue.append(right_node)

            i += 2

        return root


   
        # nodes = [None] * len(node_vals)

        # for i in range(len(node_vals)):
        #     if node_vals[i] != "x":
        #         nodes[i] = TreeNode(int(node_vals[i]))

        # for i in range(len(nodes)):
        #     if nodes[i] is not None:    
        #         if i*2+1 < len(nodes):
        #             nodes[i].left = nodes[i*2+1]
                
        #         if i*2+2 < len(nodes):
        #             nodes[i].right = nodes[i*2+2]

        # return nodes[0]
            
