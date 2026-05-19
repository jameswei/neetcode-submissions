class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_step = [0] * (n+1)
        ways_to_step[1] = 1
        ways_to_step[2] = 2

        for i in range(3, len(ways_to_step)):
            ways_to_step[i] = ways_to_step[i-1] + ways_to_step[i-2]
        
        return ways_to_step[n]