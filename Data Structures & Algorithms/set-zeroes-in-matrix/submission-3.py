class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero = False
        first_col_has_zero = False

        if matrix[0][0] == 0:
            first_col_has_zero = True
            first_row_has_zero = True

        if not first_row_has_zero:
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    first_row_has_zero = True

        if not first_col_has_zero:
            for i in range(1, len(matrix)):
                if matrix[i][0] == 0:
                    first_col_has_zero = True

        print(f"matrix: {matrix}")

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        print(f"matrix: {matrix}")

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
                

        

                
        
        