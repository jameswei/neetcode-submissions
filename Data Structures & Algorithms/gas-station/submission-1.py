class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start in range(n):
            remaining = 0
            cur_pos = start

            while True:

                remaining += gas[cur_pos]
                remaining -= cost[cur_pos]

                if remaining < 0:
                    # 不管start在哪，从 cur_pos 开不出去
                    break
                
                # 可以开到 cur_pos+1
                cur_pos += 1

                # 要绕一圈，所以如果走到末尾了要重置 cur_pos 到开头
                if cur_pos > n-1:
                    cur_pos = cur_pos % n

                if cur_pos == start:
                    return start
                
                
        return -1