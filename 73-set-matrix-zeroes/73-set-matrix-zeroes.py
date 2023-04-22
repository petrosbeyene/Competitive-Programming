class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def replace(i, j, matrix):
            for k in range(len(matrix)):
                matrix[k][j] = 0
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
        
        zeroCordinates = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroCordinates.append((i, j))
        
        for tuple in zeroCordinates:
            i, j = tuple
            replace(i, j, matrix)

        return matrix

