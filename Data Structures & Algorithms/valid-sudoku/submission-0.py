class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board[i][j] is 1-9 or '.'
        chars_in_rows = [set() for _ in range(len(board))]
        chars_in_cols = [set() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in chars_in_rows[i] or board[i][j] in chars_in_cols[j]:
                    return False
                
                chars_in_rows[i].add(board[i][j])
                chars_in_cols[j].add(board[i][j])

        print(f"chars_in_rows: {chars_in_rows}")
        print(f"chars_in_cols: {chars_in_cols}")

        m, n = 0, 0
        for k in range(9):
            # 0,1,2 : 0,3,6
            # 3,4,5 : 0,3,6
            # 6,7,8 : 0,3,6
            chars_in_sub_box = set()
            m, n = (k//3)*3, (k%3)*3
            print(f"k: {k}, m: {m}, n: {n}")

            for i in range(m, m+3):
                for j in range(n, n+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in chars_in_sub_box:
                        return False
                    # if board[i][j] in chars_in_rows[i] or board[i][j] in chars_in_cols[j]:
                    #     return False
                    chars_in_sub_box.add(board[i][j])
                
            

        return True