class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def in_bound(rw, cl, grid2):
            m, n = len(grid2), len(grid2[0])
            return (0 <= rw < m) and (0 <= cl < n)

        def dfs(visited, rw, cl):
            if not in_bound(rw, cl, grid2):
                return 
            if (rw, cl) in visited or grid2[rw][cl] == 0:
                return
            
            visited.add((rw, cl))
            grid2[rw][cl] = 0
            dfs(visited, rw+1, cl)
            dfs(visited, rw-1, cl)
            dfs(visited, rw, cl+1)
            dfs(visited, rw, cl-1)
        
        def isSubIsland(visited):
            for pos in visited:
                rw, cl = pos
                if grid1[rw][cl] == 0:
                    return False
            
            return True
        
        cnt = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    visited = set()
                    dfs(visited, i, j)
                    if isSubIsland(visited):
                        cnt += 1
        
        return cnt


