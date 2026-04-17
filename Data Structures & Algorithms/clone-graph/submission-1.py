"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        cloned_nodes = {}

        def bfs(node):
            queue = deque()

            queue.append(node)
            cloned_nodes[node] = Node(node.val)

            while len(queue) > 0:
                for i in range(len(queue)):
                    orig_node = queue.popleft()

                    for n in orig_node.neighbors:
                        if n not in cloned_nodes:
                            cloned_nodes[n] = Node(n.val)
                            queue.append(n)
                        cloned_nodes[orig_node].neighbors.append(cloned_nodes[n])
                        
                    
        bfs(node)
        return cloned_nodes[node]


            
            