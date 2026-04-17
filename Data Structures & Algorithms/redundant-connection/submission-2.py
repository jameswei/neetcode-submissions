class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [x for x in range(len(edges)+1)]
        
        def find(x: int):
            while parents[x] != x:
                x = parents[x]
            
            return parents[x]

        def union(x: int, y: int) -> bool:
            par_x = find(x)
            par_y = find(y)
            # 有共同 parent，合并失败
            if par_x == par_y:
                return False
            
            # 把 y 合并进 x
            parents[par_y] = par_x
            return True
            
        for edge in edges:
            x, y = edge[0], edge[1]
            if not union(x, y):
                return [x, y]

        return []
