class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        min_jump, max_jump = minJump, maxJump
        
        def dfs(i: int, path: list[int]) -> bool:
            if i == n-1:
                return True

            nearest = i+min_jump
            furthest = min(i+max_jump, n-1)
            print(f"from {i} can jump [{nearest}, {furthest}]")

            for j in range(nearest, furthest+1):
                if s[j] == '0':
                    path.append(j)
                    if dfs(j, path):
                        return True
                    path.pop()

            return False

        return dfs(0, [])