class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # 单调增
        coins.sort()
        res = []

        def dfs(i: int, total: int, path: list[int]):
            if total == amount:
                res.append(path[:])

            for j in range(i, len(coins)):
                val = coins[j]

                if val > amount - total:
                    break
                path.append(val)
                dfs(j, total+val, path)
                path.pop()

        dfs(0, 0, [])

        return len(res)
