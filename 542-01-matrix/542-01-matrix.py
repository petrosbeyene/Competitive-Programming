class Solution:
    def in_bound(self, i, j, mat):
        return (0<= i < len(mat)) and (0<= j < len(mat[0]))

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        q = deque()
        visited = set()
        ans = [[0] * cols for _ in range(rows)]
        
        # start BFS from all cells with value 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        # perform BFS
        distance = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                # check neighbors
                for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                    if self.in_bound(ni, nj, mat) and (ni, nj) not in visited:
                        ans[ni][nj] = distance
                        q.append((ni, nj))
                        visited.add((ni, nj))
                        
            distance += 1
                        
        return ans
