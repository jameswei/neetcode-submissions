class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero = False
        first_col_has_zero = False

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                matrix[0][j] = 1

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                matrix[i][0] = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[i])
            if first_col_has_zero:
                matrix[i][0] = 0
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

            if first_row_has_zero:
                matrix[0][j] = 0
                

        

                
        
        