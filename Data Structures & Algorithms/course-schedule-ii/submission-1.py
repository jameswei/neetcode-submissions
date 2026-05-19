class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a, b], b is dependence
        if len(prerequisites) == 0:
            return [n for n in range(numCourses)]

        courses_no_pre = set([n for n in range(numCourses)])
        
        # 构造 graph，
        # key 是前序课，val 是解锁的课程
        graph = defaultdict(list)
        for pre in prerequisites:
            if pre[0] in courses_no_pre:
                courses_no_pre.remove(pre[0])
            
            graph[pre[1]].append(pre[0])

        print(f"courses_no_pre: {courses_no_pre}, graph: {graph}")
        
        # 所有课程都有依赖，那就没法上
        if len(courses_no_pre) == 0:
            return []

        schedule = []
        # 从没有依赖的开始，本质是个层序遍历 bfs，dfs也可以
        queue = deque(courses_no_pre)

        while len(queue) > 0 and len(schedule) < numCourses:

            for _ in range(len(queue)):
                course = queue.popleft()
                if course not in schedule:
                    schedule.append(course)

                for n_c in graph[course]:
                    queue.append(n_c)

        return schedule if len(schedule) == numCourses else []


        