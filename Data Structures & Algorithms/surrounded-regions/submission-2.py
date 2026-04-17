class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        all_o_list = set()
        border_o_list = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    all_o_list.add((i, j))
                    if i == 0 or i == m-1 or j == 0 or j == n-1:
                        border_o_list.add((i, j))

        def dfs(i: int, j: int, all_o: set[tuple[int, int]]):
            if (i, j) in all_o:
                all_o.remove((i, j))


            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and board[ni][nj] == 'O' and (ni,nj) in all_o:
                    dfs(ni, nj, all_o)

            return

        for i, j in border_o_list:
            dfs(i, j, all_o_list)
        
        for i, j in all_o_list:
            board[i][j] = 'X'

        return