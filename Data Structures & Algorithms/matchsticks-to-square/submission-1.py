class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 要求使用所有值，类似于全排列
        # 但题目要求构成“正方形”，全部元素求和必须能被4整除，而且除4就是每条边的值
        # 同时正方形需要4个边构成，所以问题本质是划分成4个等和子集，每个子集和是边长

        matchsticks.sort()
        n = len(matchsticks)

        max_val = max(matchsticks)
        total_sum = sum(matchsticks)
        side_length = total_sum // 4
        
        if total_sum % 4 != 0 or max_val > side_length:
            return False

        # 划分等和k个子集，设置k个slot，但每个slot并不是定长
        sides = [0] * 4
        
        # 纯暴力解法
        def dfs(i: int) -> bool:
            if i == n:
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for j in range(4):
                if sides[j] + matchsticks[i] > side_length:
                    continue

                if j > 0 and sides[j] > sides[j-1]:
                    break
                
                # 将[i]选进[j]这条边
                sides[j] += matchsticks[i]
                if dfs(i+1):
                    return True
                sides[j] -= matchsticks[i]
                
            return False

        return dfs(0)