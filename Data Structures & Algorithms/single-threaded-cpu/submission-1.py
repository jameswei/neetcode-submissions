class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # task: [start, duration]

        task_order = []

        # (start, task_id)
        available_tasks = []
        # (duration, task_id)
        shortest_tasks = []

        cur_time = 2**31-1
        for i, t in enumerate(tasks):
            cur_time = min(cur_time, t[0])
            heapq.heappush(available_tasks, (t[0], i))

        print(f"cur_time: {cur_time}")

        while len(available_tasks) > 0 or len(shortest_tasks) > 0:

            # 当前可执行的task
            while len(available_tasks) > 0 and available_tasks[0][0] <= cur_time:
                _, task_id = heapq.heappop(available_tasks)
                duration = tasks[task_id][1]
                heapq.heappush(shortest_tasks, (duration, task_id))

            if len(shortest_tasks) > 0:
                duration, task_id = heapq.heappop(shortest_tasks)

                task_order.append(task_id)
                cur_time = cur_time + duration

        return task_order