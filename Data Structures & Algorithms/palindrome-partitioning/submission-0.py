class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]

        res = []

        def palindrom(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i: int, path: list[str]):
            if i > len(s)-1:
                res.append(path[:])
                return
            
            for j in range(i, len(s)):
                if not palindrom(i, j):
                    continue

                path.append(s[i:j+1])
                dfs(j+1, path)
                path.pop()

        dfs(0, [])
        return res
