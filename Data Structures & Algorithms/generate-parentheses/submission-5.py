class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(total: int, l_c: int, r_c: int, path: list[str]):
            if total == n * 2:
                res.append(''.join(path))
                return

            if l_c < n:
                path.append('(')
                dfs(total+1, l_c+1, r_c, path)
                path.pop()
            
            if r_c < l_c:
                path.append(')')
                dfs(total+1, l_c, r_c+1, path)
                path.pop()

        dfs(0, 0, 0, [])
        return res