class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # no any prerequisites
        if len(prerequisites) == 0:
            return True

        # 只要有循环依赖，那就不可能完成
        # 遍历 prerequisites 创建有向图，节点代表course，有向边代表依赖，0—>1，完成0课程才能完成1课程
        
        # numCourses=3
        # prerequisites=[[1,0],[0,2],[2,1]]
        # |-------|
        # | x x T |
        # | T x x |
        # | x T x |
        # |-------|

        nodes = [[0] * numCourses for _ in range(numCourses)]

        for p in prerequisites:
            c1, c2 = p[0], p[1]
            nodes[c1][c2] = 1

        def dfs(row: int, prev_course: Set) -> bool:
            if row in prev_course:
                return False
            
            prev_course.add(row)
            for i in range(len(nodes[row])):
                if nodes[row][i] == 0:
                    continue

                if not dfs(i, prev_course):
                    return False
            
            return True

        return dfs(0, set())