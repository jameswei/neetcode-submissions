class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 几个重要优化：
        # 两个方向的转动逻辑，可以统一成取模操作
        # 双向BFS，同时从init_state往target_state，从target_state往init_state。
        # 注意这不是多源BFS，而是两个独立的同时进行的BFS过程，结束的条件是，任何一方遇到了另一方已经探索过的路径。
        # 避免字符串拼接，将字符串都变成list，修改list，再转成字符串。
        # 或者直接以数字的方式操作

        dead_states = set(deadends)
        if target in dead_states:
            return -1

        init_state = "0000"
        if init_state == target:
            return 0


        forward_tried_states = {init_state: 0}
        backward_tried_states = {target: 0}
        
        forward_queue = deque([init_state])
        backward_queue = deque([target])

        while len(forward_queue) > 0 and len(backward_queue) > 0:

            for _ in range(len(forward_queue)):
                state = forward_queue.popleft()
                steps = forward_tried_states[state]
                
                cur_state = list(state)

                for i in range(4):
                    digit = int(cur_state[i])

                    for turn in [1, -1]:
                        new_digit = (digit+turn)%10
                        cur_state[i] = str(new_digit)
                        
                        new_state = ''.join(cur_state)

                        if new_state in dead_states or new_state in forward_tried_states:
                            continue

                        if new_state in backward_tried_states:
                            return steps + 1 + backward_tried_states[new_state]

                        forward_queue.append(new_state)
                        forward_tried_states[new_state] = steps+1

                    # 恢复回去
                    cur_state[i] = str(digit)

            for _ in range(len(backward_queue)):
                state = backward_queue.popleft()
                steps = backward_tried_states[state]

                cur_state = list(state)

                for i in range(4):
                    digit = int(cur_state[i])

                    for turn in [1, -1]:
                        new_digit = (digit+turn)%10
                        cur_state[i] = str(new_digit)

                        new_state = ''.join(cur_state)

                        if new_state in dead_states or new_state in backward_tried_states:
                            continue
                        
                        if new_state in forward_tried_states:
                            return steps + 1 + forward_tried_states[new_state]

                        backward_queue.append(new_state)
                        backward_tried_states[new_state] = steps+1

                    cur_state[i] = str(digit)

        return -1