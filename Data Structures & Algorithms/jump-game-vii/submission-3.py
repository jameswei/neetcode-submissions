class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        min_jump, max_jump = minJump, maxJump
        memo = {}
        
        def dfs(i: int, path: list[int]) -> bool:
            if i == n-1:
                return True

            if i in memo:
                return memo[i]

            nearest = i+min_jump
            furthest = min(i+max_jump, n-1)

            for j in range(nearest, furthest+1):
                if s[j] == '0':
                    path.append(j)
                    if dfs(j, path):
                        memo[i] = True
                        return True
                    path.pop()

            memo[i] = False
            return False

        return dfs(0, [])