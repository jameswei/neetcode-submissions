"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        cloned_nodes = {}

        def dfs(node) -> Optional[Node]:
            if node in cloned_nodes:
                return cloned_nodes[node]

            clone_node = Node(node.val)
            cloned_nodes[node] = clone_node

            if len(node.neighbors) == 0:
                clone_node.neighbors = []
                return clone_node
            
            neighbors_of_clone_node = []
            for n in node.neighbors:
                neighbors_of_clone_node.append(dfs(n))
            
            # 后序思路
            clone_node.neighbors = neighbors_of_clone_node
            
            return clone_node

        return dfs(node)


            
            