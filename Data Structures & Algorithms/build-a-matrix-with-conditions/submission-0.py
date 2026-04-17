class Solution:
    def buildMatrix(
            self, 
            k: int, 
            rowConditions: List[List[int]], 
            colConditions: List[List[int]]
        ) -> List[List[int]]:
        # row_conditions和col_conditions本质上是两个约束
        # 给定的[above[i],below[i]]表示above[i]必须在below[i]的上面行
        # 而[left[j],right[j]]表示left[i]必须在right[i]的后面列
        # 这种顺序的约束，可以转化成有向边，而值可以转化成顶点
        # 所以这道题变成了有向图的路径问题
        # 再进一步每一个row_condition和col_condition都是局部顺序，需要建立出全局顺序

        row_adj = defaultdict(list)
        row_indegree = defaultdict(int)
        for r_con in rowConditions:
            row_adj[r_con[0]].append(r_con[1])
            row_indegree[r_con[1]] += 1

        row_queue = deque()
        for val in range(1, k+1):
            if row_indegree[val] == 0:
                row_queue.append(val)

        if len(row_queue) == 0:
            return []
            
        col_adj = defaultdict(list)
        col_indegree = defaultdict(int)
        for col_con in colConditions:
            col_adj[col_con[0]].append(col_con[1])
            col_indegree[col_con[1]] += 1

        col_queue = deque()
        for val in range(1, k+1):
            if col_indegree[val] == 0:
                col_queue.append(val)

        if len(col_queue) == 0:
            return []

        val_in_row = []
        while len(row_queue) > 0:
            val = row_queue.popleft()
            val_in_row.append(val)

            for another_val in row_adj[val]:
                row_indegree[another_val] -= 1
                if row_indegree[another_val] == 0:
                    row_queue.append(another_val)

        print(f"val_in_row: {val_in_row}")

        val_in_col = []
        while len(col_queue) > 0:
            val = col_queue.popleft()
            val_in_col.append(val)

            for another_val in col_adj[val]:
                col_indegree[another_val] -= 1
                if col_indegree[another_val] == 0:
                    col_queue.append(another_val)

        print(f"val_in_col: {val_in_col}")

        res = []

        for i in range(k):
            # prefill as [0,...,0]
            row = [0 for _ in range(k)]
            for j in range(k):
                if val_in_row[i] == val_in_col[j]:
                    row[j] = val_in_col[j]
                    break

            res.append(row)

        return res