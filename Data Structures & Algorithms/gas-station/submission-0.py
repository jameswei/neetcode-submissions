class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 单个 station 的情况
        if len(gas) == 1:
            return 0 if gas[0] > cost[0] else -1

        # 朴素思路
        # 每一个station尽可能多加油，少花销，就能走得更远
        # 只有当剩余油不够花销时就会停下
        # 考虑的是能否顺时针回到起点，那在每一站都继续加油，尽量让剩余油越多越好

        # 选择“油-花销”差值最大的station作为起点
        n = len(gas)
        total_gas = total_cost = 0

        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            if total_gas > total_cost:
                return i

        return -1
            

        



        

        