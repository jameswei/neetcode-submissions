class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        
        m, n = len(matrix), len(matrix[0])
        self._prefix_sum = [[0] * n for _ in range(m)]

        for i in range(m):
            p_sum = 0
            for j in range(n):
                p_sum += self._matrix[i][j]
                self._prefix_sum[i][j] = p_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_of_region = 0

        for i in range(row1, row2+1):
            sum_of_region += (self._prefix_sum[i][col2]-self._prefix_sum[i][col1]+self._matrix[i][col1])

        return sum_of_region        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)