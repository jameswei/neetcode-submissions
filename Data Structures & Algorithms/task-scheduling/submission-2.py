class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for t in tasks:
            task_count[t] += 1

        # 前者是频次优先级队列，根据初始给定任务列表填充，当任务被执行一次后就不再使用
        # 后者是等待时间优先级队列，根据下次执行时间填充，执行过一次任务都在此队列
        most_frequent_task = []
        cool_down_task = []

        for k, v in task_count.items():
            heapq.heappush(most_frequent_task, (-1*v, k))

        cycle = 0

        while len(most_frequent_task) > 0 or len(cool_down_task) > 0:
            while len(cool_down_task) > 0 and cool_down_task[0][0] <= cycle:
                _, task = heapq.heappop(cool_down_task)
                heapq.heappush(most_frequent_task, (-1*task_count[task], task))
            
            if len(most_frequent_task) > 0:
                cnt, task = heapq.heappop(most_frequent_task)
                task_count[task] -= 1

                if task_count[task] > 0:
                    next_cycle = cycle+n+1
                    heapq.heappush(cool_down_task, (next_cycle, task))
            
            cycle += 1
        
        
        return cycle