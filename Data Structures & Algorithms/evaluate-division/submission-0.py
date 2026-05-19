class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 建图+dfs
        # 每个equation就代表变量a到b有一条边，边的权重是b/a的结果；反过来也有一条边从b到a，权重是a/b
        
        adj_table = defaultdict(list)

        for i in range(len(equations)):
            var_1, var_2, val = equations[i][0], equations[i][1], values[i]
            adj_table[var_2].append((var_1, val))
            adj_table[var_1].append((var_2, 1/val))

        print(f"adj_table: {adj_table}")

        # dfs搜索的目的是找给定两点的可达路径，路径中都是乘积
        def dfs(var_1: str, var_2: str, visited: set[str]) -> float:
            if var_1 == var_2:
                return 1

            for (var, mutiplier) in adj_table[var_1]:
                if var not in visited:
                    visited.add(var)
                    val = dfs(var, var_2, visited)
                    if val != -1:
                        return mutiplier*val

            return -1

        res = []
        for q in queries:
            var_1, var_2 = q[0], q[1]

            if var_1 == var_2:
                res.append(1)
                continue

            if var_1 not in adj_table or var_2 not in adj_table:
                res.append(-1)
                continue
            
            res.append(dfs(var_2, var_1, set([var_2])))

        return res