class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]

        res = []

        i_bound = [-1, len(matrix)]
        j_bound = [-1, len(matrix[0])]
        i, j = 0, 0
        print(f"i_bound: {i_bound}, j_bound: {j_bound}, i: {i}, j: {j}")

        while i_bound[0]<i<i_bound[1] and j_bound[0]<j<j_bound[1]:

            while j < j_bound[1]:
                res.append(matrix[i][j])
                j += 1
            
            print(f"{res}")

            if j == j_bound[0]+1 or i == i_bound[1]-1:
                break

            # reset j
            j -= 1
            # update i_bound[0]
            i_bound[0] = i
            i += 1

            print(f"i_bound: {i_bound}, j_bound: {j_bound}, i: {i}, j: {j}")

            while i < i_bound[1]:
                res.append(matrix[i][j])
                i += 1

            print(f"{res}")

            if i == i_bound[0]+1 or j==j_bound[0]+1:
                break

            # reset i
            i -= 1
            # update j_bound[1]
            j_bound[1] = j
            j -= 1

            print(f"i_bound: {i_bound}, j_bound: {j_bound}, i: {i}, j: {j}")

            while j > j_bound[0]:
                res.append(matrix[i][j])
                j -= 1

            print(f"{res}")

            if j == j_bound[1]-1 or i == i_bound[0]+1:
                break

            # reset j
            j += 1
            # update i_bound[1]
            i_bound[1] = i
            i -= 1

            print(f"i_bound: {i_bound}, j_bound: {j_bound}, i: {i}, j: {j}")

            while i > i_bound[0]:
                res.append(matrix[i][j])
                i -= 1

            print(f"{res}")

            if i == i_bound[1]-1 or j == j_bound[1]-1:
                break

            # reset i
            i += 1
            # update j_bound[0]
            j_bound[0] = j
            j += 1

            print(f"i_bound: {i_bound}, j_bound: {j_bound}, i: {i}, j: {j}")


        return res