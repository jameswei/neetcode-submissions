class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for t in tasks:
            task_count[t] += 1

        most_frequent_task = []
        for k, v in task_count.items():
            heapq.heappush(most_frequent_task, (-1*v, k))

        cycle = 0
        task_executed_at = defaultdict(lambda: -1)

        while len(most_frequent_task) > 0:
            # 从堆顶 pop 出来
            (count, task) = heapq.heappop(most_frequent_task)
            
            minus = 0

            last_exec = task_executed_at[task]
            # 还没执行过
            if last_exec == -1:
                # 执行，减个数，放回去
                task_executed_at[task] = cycle
                minus = 1

            # 执行过，冷却也够了
            elif cycle - last_exec > n:
                # 执行，减个数，放回去
                task_executed_at[task] = cycle
                minus = 1

            # 只有上述情况可以执行当前取出的任务，
            # 但是不代表没有任务可以执行，应该继续取别的任务
            else:
                temp = []

                while len(most_frequent_task) > 0:
                    next_task = heapq.heappop(most_frequent_task)
                    last_exec = task_executed_at[next_task[1]]

                    if last_exec == -1 or cycle-last_exec > n:
                        task_executed_at[next_task[1]] = cycle
                        if next_task[0]+1 != 0:
                            heapq.heappush(most_frequent_task, (next_task[0]+1, next_task[1]))
                        break

                    temp.append(next_task)

                # 原模原样放回去
                if len(temp) > 0:
                    for t in temp:
                        heapq.heappush(most_frequent_task, t)


            # push 回去之前检查下该种任务是否全结束了
            if count + minus != 0:
                heapq.heappush(most_frequent_task, (count+minus, task))

            cycle += 1
        
        return cycle