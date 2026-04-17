class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 转置：沿着主对角线（left-top到bottom-right）反转矩阵
        # 主对角线任意元素abs(i-j)是常数

        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]


        return transposed