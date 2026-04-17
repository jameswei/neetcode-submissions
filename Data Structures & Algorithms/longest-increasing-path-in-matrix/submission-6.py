class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 记忆化dfs 转成 dp 解法，对于这道题比较特殊
        # 它的状态依然等同于记忆化的抽象，也就是dp[i][j]是matrix[i][j]做起点可达的增长路径长度的最大长度
        # 所以状态转移方程也就和 dfs 递归中计算方式一样
        # dp[i][j] = max(dp[n_i][n_j]...)，要求matrix[n_i][n_j]>matrix[i][j]‘
        # 但是！这种情况下dp表格计算没法像通常的按顺序计算，比如从左到右从上到下
        # 因为它依赖的是4个方向上更大值的位置，不是固定顺序。
        m, n = len(matrix), len(matrix[0])

        # dp 状态定义和记忆化+dfs一致
        # 区别是初始情况下单一节点的最长增长路径的长度都是1，就是自身
        dp = [[1] * n for _ in range(m)]

        val_pos = []
        # 对 matrix 值进行排序
        for i in range(m):
            for j in range(n):
                heapq.heappush(val_pos, (-1*matrix[i][j], (i, j)))

        longest_len = 1
        
        # 遍历，从大到小
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(val_pos) > 0:
            _, (i, j) = heapq.heappop(val_pos)
            
            for (d_i, d_j) in dirs:
                n_i, n_j = i+d_i, j+d_j
                if 0<=n_i<m and 0<=n_j<n and matrix[n_i][n_j] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[n_i][n_j]+1)

            longest_len = max(longest_len, dp[i][j])

        return longest_len