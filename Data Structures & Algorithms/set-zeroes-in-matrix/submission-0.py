class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        t_i, t_j = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                val = matrix[i][j]
                if val == 0:
                    t_i.append(i)
                    t_j.append(j)
            
        for i in t_i:
            matrix[i] = [0] * len(matrix[i])
        
        for j in t_j:
            for i in range(len(matrix)):
                matrix[i][j] = 0
                
        
        