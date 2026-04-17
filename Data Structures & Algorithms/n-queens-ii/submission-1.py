class Solution:
    def totalNQueens(self, n: int) -> int:
        # 相比N-Queens问题，只需返回有效解的个数
        if n == 1:
            return 1

        placed_col = [False] * n
        placed_main_diag = [False] * (2*n-1)
        placed_sec_diag = [False] * (2*n-1)

        def dfs(row: int) -> int:
            if row == n:
                return 1

            total_placement = 0
            for col in range(n):
                if not placed_col[col] and not placed_main_diag[row-col+n-1] and not placed_sec_diag[row+col]:
                    placed_col[col] = True
                    placed_main_diag[row-col+n-1] = True
                    placed_sec_diag[row+col] = True

                    total_placement += dfs(row+1)

                    placed_col[col] = False
                    placed_main_diag[row-col+n-1] = False
                    placed_sec_diag[row+col] = False

            return total_placement

        return dfs(0)
