class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        # 组合问题

        digit_to_char = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
        }
        

        res = []

        def dfs(i: int, path: list[str]):
            if i > len(digits)-1 or len(path) == len(digits):
                res.append(''.join(path))
                return
            
            num = int(digits[i])

            for c in digit_to_char[num]:
                path.append(c)
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res