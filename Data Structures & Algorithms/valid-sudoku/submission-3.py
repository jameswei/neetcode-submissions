class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums_in_rows = [0b0] * len(board)
        nums_in_cols = [0b0] * len(board)
        nums_in_boxes = [0b0] * len(board)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j]) - 1
                mask = 0b1 << num

                if mask & nums_in_rows[i] or mask & nums_in_cols[j]:
                    return False

                if mask & nums_in_boxes[(i//3)*3+(j//3)]:
                    return False

                nums_in_rows[i] = nums_in_rows[i] | mask
                nums_in_cols[j] = nums_in_cols[j] | mask
                nums_in_boxes[(i//3)*3+(j//3)] = nums_in_boxes[(i//3)*3+(j//3)] | mask

        return True