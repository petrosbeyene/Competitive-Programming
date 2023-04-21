class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        new_mat = [[0] * c for _ in range(r)]
        
        index = 0
        for i in range(r):
            for j in range(c):
                row, col = divmod(index, n)
                new_mat[i][j] = mat[row][col]
                index += 1
                
        return new_mat
