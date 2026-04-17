class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prerequisites[i][0]->prerequisites[i][1]，依赖关系代表有向边
        # 给定queries[j]，判断queries[j][0]是否->queries[j][1]
        # 也就是只检查连通性，给定元素是否属于一个连通量
        # 先用建图+dfs解法

        adj_table = defaultdict(list)
        indegree_table = defaultdict(int)

        for pre, suc in prerequisites:
            adj_table[pre].append(suc)
            indegree_table[suc] += 1

        def dfs(a: int, b: int, visited: set[int]) -> bool:
            if a == b:
                return True
            
            successors = adj_table[a]

            for suc in successors:
                if suc not in visited:
                    visited.add(suc)
                    if dfs(suc, b, visited):
                        return True

            return False

        res = []

        for a, b in queries:
            if a not in adj_table or indegree_table[b] == 0:
                res.append(False)
                continue

            res.append(dfs(a, b, set([a])))
        
        return res