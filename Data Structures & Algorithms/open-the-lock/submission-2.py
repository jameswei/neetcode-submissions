class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 从图的角度来思考
        # 把锁的状态当成图中的节点
        # 找解开锁（达到特定状态）的最少转动次数，本质就变成图遍历中到达符合条件节点的最短路径问题
        
        dead_states = set(deadends)
        init_lock_state = "0000"

        if init_lock_state in dead_states:
            return -1

        if init_lock_state == target:
            return 0
        
        # bfs遍历找最短路径
        queue = deque([(init_lock_state, 0)])
        turn = [1, -1]
        tried_states = set([init_lock_state])

        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                lock_state, steps = queue.popleft()

                # 4位
                for i in range(4):
                    code = int(lock_state[i])

                    for t in turn:
                        new_code = code + t
                        if new_code < 0:
                            new_code = 9
                        if new_code > 9:
                            new_code = 0
                        
                        new_lock_state = lock_state[0:i]+str(new_code)+lock_state[i+1:]

                        if new_lock_state == target:
                            return steps + 1 
                        
                        if new_lock_state not in dead_states and new_lock_state not in tried_states:
                            queue.append((new_lock_state, steps + 1))
                            tried_states.add(new_lock_state)

        return -1