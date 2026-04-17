class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(board: List[List[str]], word: str, idx: int, i: int, j: int, cells: List[List[int]]) -> bool:
            # fully matched
            if idx == len(word):
                return True
            
            # out of boundary
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[i]):
                return False

            # was matched before
            if [i, j] in cells:
                return False
            
            cur_char = board[i][j]
            target_char = word[idx]

            if cur_char != target_char:
                return False
            
            cells.append([i, j])
            
            right = dfs(board, word, idx+1, i, j+1, cells)
            left = dfs(board, word, idx+1, i, j-1, cells)
            down = dfs(board, word, idx+1, i+1, j, cells)
            up = dfs(board, word, idx+1, i-1, j, cells)

            cells.pop()
            return right or left or down or up

            
        for m in range(len(board)):
            for n in range(len(board[m])):
                found = dfs(board, word, 0, m, n, list())
                if found:
                    return True
        return False