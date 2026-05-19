class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # no any prerequisites
        if len(prerequisites) == 0:
            return True

        # 只要有循环依赖，那就不可能完成
        # n 门课，设置一个n*n 矩阵
        # 遍历prerequisites，设置课之间的依赖
        # 矩阵设置完成后，再遍历如果[i][j]和[j][i]==True，就有依赖

        courses_dep = [[False] * numCourses for _ in range(numCourses)]

        for p in prerequisites:
            c1, c2 = p[0], p[1]
            courses_dep[c1][c2] = True
            # found loop dependency
            if courses_dep[c2][c1]:
                return False
        
        return True