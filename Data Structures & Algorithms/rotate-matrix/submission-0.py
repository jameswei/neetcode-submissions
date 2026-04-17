class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # rotate rows from head to last
        for i in range(n // 2):
            from_row = matrix[i]
            to_row = matrix[n-1-i]

            matrix[i] = to_row
            matrix[n-1-i] = from_row

        # swap cell from upper-right to bottom-left
        for i in range(n):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        