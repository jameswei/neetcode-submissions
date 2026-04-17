class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]

        placed_row = [False] * n
        placed_col = [False] * n
        placed_main_diagonal = [False] * (2*n-1)
        placed_secondary_diagonal = [False] * (2*n-1)

        def can_placed(row: int, col: int) -> bool:
            if placed_row[row]:
                return False

            if placed_col[col]:
                return False

            if placed_main_diagonal[(row-col)+(n-1)]:
                return False

            if placed_secondary_diagonal[(row+col)]:
                return False

            return True

        res = []

        def dfs(row: int, path: list[str]):
            if row > n-1 or len(path) == n:
                res.append(path[:])
                return
            
            for col in range(n):
                row_path = ['.'] * n

                if can_placed(row, col):
                    row_path[col] = 'Q'
                    path.append(''.join(row_path))
                    placed_row[row] = True
                    placed_col[col] = True
                    placed_main_diagonal[(row-col)+(n-1)] = True
                    placed_secondary_diagonal[(row+col)] = True

                    dfs(row+1, path)

                    path.pop()
                    placed_row[row] = False
                    placed_col[col] = False
                    placed_main_diagonal[(row-col)+(n-1)] = False
                    placed_secondary_diagonal[(row+col)] = False


        dfs(0, [])
        return res