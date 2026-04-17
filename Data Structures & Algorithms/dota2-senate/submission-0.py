class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 按照senate中的顺序轮流投票，队列可以确保FIFO特性
        radiant_queue = deque()
        dire_queue = deque()

        for i in range(len(senate)):
            char = senate[i]
            if char == 'R':
                radiant_queue.append(i)
            elif char == 'D':
                dire_queue.append(i)

        n = len(senate)

        while len(radiant_queue) > 0 and len(dire_queue) > 0:
            radiant_pos = radiant_queue.popleft()
            dire_pos = dire_queue.popleft()
            if radiant_pos > dire_pos:
                dire_queue.append(dire_pos+n)
            elif radiant_pos < dire_pos:
                radiant_queue.append(radiant_pos+n)

        return "Radiant" if len(radiant_queue) > 0 else "Dire"