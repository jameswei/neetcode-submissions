class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix)*len(matrix[0])

        while i <= j and -1 < i < len(matrix)*len(matrix[0]) and -1 < j < len(matrix)*len(matrix[0]):
            mid = i+(j-i)//2
            print(f"i:{i}, j:{j}, mid:{mid}")
            num = matrix[mid//len(matrix)][mid%len(matrix[0])]

            if target == num:
                return True
            elif target < num:
                j = mid - 1
            else:
                i = mid + 1
        
        return False