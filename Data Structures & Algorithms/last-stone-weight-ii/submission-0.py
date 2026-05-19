class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 要求返回尽可能小的剩余重量
        # 那最理想情况就是每两个都消除，并且保证整下的是较小的重量
        # 更深刻的观察是：分成两堆，让两堆的重量尽可能接近（这样碰撞后才能要么消除要么剩下的小）
        # 而分成两堆同时又尽可能接近，那理想情况是总重量的一半

        n = len(stones)
        total_weight = sum(stones)
        # ideal_weight就是target
        ideal_weight = total_weight//2
        
        # 记忆化+dfs
        # 穷举所有选择，避免重复计算
        def dfs(i: int, total: int):
            if total >= ideal_weight or i == n:
                return abs(total - (total_weight-total))

            return min(dfs(i+1, total+stones[i]), dfs(i+1, total))

        return dfs(0, 0)