class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 优化一：
        # 按单调减排序，先对大的matchstick进行尝试，符合fail-fast的原则
        matchsticks.sort(reverse=True)

        n = len(matchsticks)

        total_sum = sum(matchsticks)
        side_length = total_sum // 4
        
        if total_sum % 4 != 0 or max(matchsticks) > side_length:
            return False

        # 划分等和k个子集，设置k个slot，但每个slot并不是定长
        sides = [0] * 4
        
        def dfs(i: int) -> bool:
            if i == n:
                return sides[0] == sides[1] == sides[2] == sides[3]

            cur_stick = matchsticks[i]
            
            for j in range(4):
                if sides[j] + cur_stick > side_length:
                    continue

                if j > 0 and sides[j] > sides[j-1]:
                    continue
                
                # 将[i]选进[j]这条边
                sides[j] += cur_stick
                if dfs(i+1):
                    return True
                sides[j] -= cur_stick
                
            return False

        return dfs(0)