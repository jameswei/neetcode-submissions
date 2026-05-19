class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 逐位像target对应位转动
        # 根据deadend的值调整转动方向
        # 根据转动方向确定转动步数
        # 最终结果就是各个位转动步数总和

        # 第[i]位的dead code
        dead_code = defaultdict(set)
        for deadend in deadends:
            for i in range(len(deadend)):
                dead_code[i].add(deadend[i])

        print(f"dead_code: {dead_code}")
        
        # 检查target的每一位是否是dead code
        for i in range(len(target)):
            # 任何一位无可能调整到就失败
            if target[i] in dead_code[i]:
                return -1
        
        inf = 2**31-1
        total_steps = 0
        lock = "0000"
        dirs = [(1, 1), (9, -1)]

        for i in range(len(lock)):
            # 已经是target值
            if lock[i] == target[i]:
                total_steps += 0
                continue

            target_val = int(target[i])
            min_steps = inf
            # 尝试两个方向
            for start_val, delta_val in dirs:
                reachable = True
                for j in range(start_val, target_val, delta_val):
                    if str(j) in dead_code[i]:
                        reachable = False
                        break
                
                if reachable:
                    min_steps = min(min_steps, abs(target_val-start_val+delta_val))
                    print(f"from {start_val} in direction {delta_val}, steps: {min_steps}")

            if min_steps == inf:
                return -1

            total_steps += min_steps


        return total_steps