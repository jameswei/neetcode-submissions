class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 本质上可以看成是一棵树多了一条边
        # 因为一棵树是全连接，现在多一条边产生某个局部环，删去多余的边后仍然是树

        nodes = set()
        connections = defaultdict(list[int])

        # 本质是 dfs 搜索
        # either from a to b or from b to a
        def connected(a: int, b: int, visited: set[int]) -> bool:
            if a in visited:
                return False

            visited.add(a)
            
            for x in connections[a]:
                if x == b:
                    return True
                
                if connected(x, b, visited):
                    return True
                
            return False

        for edge in edges:
            if (edge[0] in nodes and 
                edge[1] in nodes and 
                (connected(edge[0], edge[1], set()) or connected(edge[1], edge[0], set()))):

                return edge
            
            nodes.add(edge[0])
            nodes.add(edge[1])
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])
        
        return []