class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # no any prerequisites
        if len(prerequisites) == 0:
            return True

        # 只要有循环依赖，那就不可能完成
        # 遍历 prerequisites 创建有向图，节点代表course，有向边代表依赖，0—>1，完成0课程才能完成1课程
        
        # numCourses=5
        # prerequisites=[[1,4],[2,4],[3,1],[3,2]]
        # {
        #   0: []
        #   1: [4]
        #   2: [4]
        #   3: [1, 2]
        #   4: []
        # }
        

        # 用邻接表
        # dict或List[List[]]都可以
        course_graph = [[] for _ in range(numCourses)]

        for p in prerequisites:
            course_graph[p[0]].append(p[1])

        print(f"course_graph: {course_graph}")

        def dfs(course: int, chain: set[int]) -> bool:
            if course in chain:
                return False

            if course_graph[course] == []:
                return True

            chain.add(course)

            for dep in course_graph[course]:
                if not dfs(dep, chain):
                    return False
            
            chain.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True

