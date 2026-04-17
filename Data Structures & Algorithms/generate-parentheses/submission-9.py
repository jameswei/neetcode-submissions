class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(l_c: int, r_c: int, path: list[str]):
            if l_c == r_c == n and len(path) == n * 2:
                res.append(''.join(path))
                return

            if l_c < n:
                path.append('(')
                dfs(l_c+1, r_c, path)
                path.pop()
            
            if r_c < l_c:
                path.append(')')
                dfs(l_c, r_c+1, path)
                path.pop()

        dfs(0, 0, [])
        return res