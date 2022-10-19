class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        
        self.prefSum = matrix 
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefSum[i][j] += self.prefSum[i][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i = row1
        j = col1
        s = 0
        while i <= row2:
            if col1 == 0:
                s += self.prefSum[i][col2]
            else:
                s += (self.prefSum[i][col2] - self.prefSum[i][j-1])
            i += 1
        
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)