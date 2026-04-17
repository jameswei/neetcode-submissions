class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 单个 station 的情况
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1

        # 朴素思路
        # 在每一站都能加油，但移动到下一站也要消耗
        # 任何时刻只要剩余油为负就会停下

        # 每一站能加的油和需要的消耗的差值，可以认为是这一站对于行程的“贡献”
        # 如果整个路径中可以加的油总量不够所有的消耗，那说明不可能完成行程

        n = len(gas)

        total_gas = total_cost = 0
        gas_in_tank = 0
        start = 0

        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]

            gas_in_tank += (gas[i]-cost[i])

            if gas_in_tank < 0:
                start = i+1
                gas_in_tank = 0
        print(f"total_gas: {total_gas}, total_cost: {total_cost}")
        if total_gas < total_cost:
            return -1
        
        return start%n