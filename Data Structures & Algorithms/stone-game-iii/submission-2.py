class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # i开始的石堆，玩家按照最优策略能获得的最大净胜分
        # 给定[i...n-1]石堆时，玩家能做的选择：拿1或2或3个，计其得分。接着在新的石堆，对手能得的分。想减就是净胜分。
        # dp[i] = max(val[i]-dp[i+1], val[i]+val[i+1]-dp[i+2], val[i]+val[i+1]+val[i+2]-dp[i+3])
        dp = [0] * n
        # 初始状态，当只剩下[n-1]石块时，取完就结束了，对手方没有新的得分机会
        dp[n-1] = stoneValue[n-1]-0
        
        for i in range (n-2, -1, -1):
            max_diff = -2**31
            max_score = 0
            for j in range(3):
                if i+j < n:
                    max_score += stoneValue[i+j]
                    max_diff = max(max_diff, max_score-(dp[i+j+1] if i+j+1<n else 0))
            dp[i] = max_diff

        if dp[0] == 0:
            return "Tie"
        else:
            return "Alice" if dp[0] > 0 else "Bob"