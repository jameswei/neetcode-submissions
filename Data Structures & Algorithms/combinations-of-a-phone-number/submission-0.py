class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        # 组合问题
        digit_to_char = defaultdict(list)
        
        start = 97
        for i in range(8):
            if i == 5 or i == 7:
                for _ in range(4):
                    digit_to_char[i+2].append(chr(start))
                    start += 1
                continue
            for _ in range(3):
                digit_to_char[i+2].append(chr(start))
                start += 1

        res = []

        def dfs(i: int, path: list[str]):
            if i > len(digits)-1:
                res.append(''.join(path))
                return
            
            num = int(digits[i])
            
            chars = digit_to_char[num]

            for j in range(len(chars)):
                c = chars[j]
                path.append(c)
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res