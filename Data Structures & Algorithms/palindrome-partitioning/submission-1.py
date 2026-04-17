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
            
            # 对于当前起点i，尝试所有可能的终点j
            for j in range(i, len(s)):
                # 如果[i,j]范围是 palindrome，那就是个有效解，
                if palindrom(i, j):
                    # 将有效解加入 path，和别的backtrack的区别就在这里，它的选择必须是一个解的情况下
                    path.append(s[i:j+1])
                    # 继续递归，但是起点变成了终点之后
                    dfs(j+1, path)
                    # 返回到这里再撤销选择，因为下一轮循环里也就是下一个路径中，可能[i,j]依然是有效解
                    path.pop()

        dfs(0, [])
        return res
