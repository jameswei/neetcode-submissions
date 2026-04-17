class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 使用 Khan 算法的解法，也就是拓扑排序
        # TODO 思考路径和解法

        m, n = len(matrix), len(matrix[0])
        pos_to_indegress = defaultdict(int)
        no_indegress_pos = deque()

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        for i in range(m):
            for j in range(n):
                for (d_i, d_j) in dirs:
                    n_i, n_j = i+d_i, j+d_j
                    if 0<=n_i<m and 0<=n_j<n and matrix[n_i][n_j] < matrix[i][j]:
                        pos_to_indegress[(i,j)] += 1

                if pos_to_indegress[(i,j)] == 0:
                    no_indegress_pos.append((i,j))


        longest_len = 0
        while len(no_indegress_pos) > 0:
            total_pos = len(no_indegress_pos)
            for _ in range(total_pos):

                (i, j) = no_indegress_pos.popleft()
                for (d_i, d_j) in dirs:
                    n_i, n_j = i+d_i, j+d_j
                    if 0<=n_i<m and 0<=n_j<n and matrix[n_i][n_j] > matrix[i][j]:
                        pos_to_indegress[(n_i,n_j)] -= 1

                        if pos_to_indegress[(n_i,n_j)] == 0:
                            no_indegress_pos.append((n_i,n_j))

            longest_len += 1
        
        return longest_len