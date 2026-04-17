class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board[i][j] is 1-9 or '.'

        for row in range(9):
            chars_in_row = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                
                if board[row][i] in chars_in_row:
                    return False

                chars_in_row.add(board[row][i])

        for col in range(9):
            chars_in_col = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue

                if board[i][col] in chars_in_col:
                    return False

                chars_in_col.add(board[i][col])


        for k in range(9):
            chars_in_sub_box = set()
            m, n = (k//3)*3, (k%3)*3

            for i in range(m, m+3):
                for j in range(n, n+3):
                    if board[i][j] == '.':
                        continue
                    
                    if board[i][j] in chars_in_sub_box:
                        return False
                    
                    chars_in_sub_box.add(board[i][j])
            

        return True