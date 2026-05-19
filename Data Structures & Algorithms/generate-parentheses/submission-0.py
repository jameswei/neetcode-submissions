class Solution:
    def is_valid(self, candidate: str) -> bool:
        balance = 0
        for c in candidate:
            if c == '(':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0


    def generateParenthesis(self, n: int) -> List[str]:
        # n pair == n*2 chars
        # after sorted，will get n left and then n right
        # like this: '((()))'
        # 类似于一个规则更严格的排列问题

        chars = []
        for i in range(n):
            chars.append('(')
            chars.append(')')

        used_chars = [False] * len(chars)

        res = set()

        def dfs(path: list[str]):

            if len(path) == len(chars):
                candidate = ''.join(path[:])
                if self.is_valid(candidate):
                    res.add(candidate)
                return

            for i in range(len(chars)):
                if used_chars[i]:
                    continue

                c = chars[i]
                path.append(c)
                used_chars[i] = True
                dfs(path)
                path.pop()
                used_chars[i] = False

        dfs([])

        return list(res)

