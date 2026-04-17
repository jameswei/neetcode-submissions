class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 几个重要优化：
        # 两个方向的转动逻辑，可以统一成取模操作
        # 双向BFS，同时从init_state往target_state，从target_state往init_state。
        # 注意这不是多源BFS，而是两个独立的同时进行的BFS过程，结束的条件是，任何一方遇到了另一方已经探索过的路径。
        # 避免字符串拼接，将字符串都变成list，修改list，再转成字符串。
        # 或者直接以数字的方式操作

        init_state = "0000"
        dead_states = set(deadends)
        if target in dead_states or init_state in dead_states:
            return -1

        if init_state == target:
            return 0


        forward_tried_states = {init_state: 0}
        backward_tried_states = {target: 0}
        
        forward_queue = deque([init_state])
        backward_queue = deque([target])

        def bfs(queue, states, other_states) -> int:
            for _ in range(len(queue)):
                state = queue.popleft()
                steps = states[state]
                
                cur_state = list(state)

                for i in range(4):
                    digit = int(cur_state[i])

                    for turn in [1, -1]:
                        new_digit = (digit+turn)%10
                        cur_state[i] = str(new_digit)
                        
                        new_state = ''.join(cur_state)

                        if new_state in dead_states or new_state in states:
                            continue

                        if new_state in other_states:
                            return steps + 1 + other_states[new_state]

                        queue.append(new_state)
                        states[new_state] = steps+1

                    # 恢复回去
                    cur_state[i] = str(digit)



        while len(forward_queue) > 0 and len(backward_queue) > 0:
            # 另一个优化点是，每层处理时，优先选择规模（在bfs中称为frontier）小的那一方。这可以控制搜索树继续增长的宽度，保证搜索的规模尽可能小。
            # 目的是让两方的搜索范围（或前沿面积）尽可能保持平衡。
            # 以社交网络的例子，节点a有10个邻居节点，节点b有1000的邻居节点，即使在不确定下一层邻居节点数量的情况下，b节点的搜索树在下一层就已经有1000宽度，而a节点的搜索树只有10宽度。
            # “扩展较小队列”就是为了动态地调整，确保两边大致齐头并进，让它们的边界以相近的速度向外扩张，从而最大化地在中间区域相遇，最小化总的探索节点数。
            res = None
            if len(forward_queue) > len(backward_queue):
                res = bfs(backward_queue, backward_tried_states, forward_tried_states)
            else:
                res = bfs(forward_queue, forward_tried_states, backward_tried_states)

            if res is not None:
                return res

        return -1