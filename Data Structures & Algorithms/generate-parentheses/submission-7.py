class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str) -> bool:
            balance = 0
            for c in s:
                balance += 1 if c == '(' else -1
                if balance < 0:
                    return False
            return balance == 0
        
        def dfs(path: list[str]):
            if len(path) == n * 2:
                if valid(''.join(path)):
                    res.append(''.join(path))
                return

            path.append('(')
            dfs(path)
            path.pop()

            path.append(')')
            dfs(path)
            path.pop()

        dfs([])
        return res