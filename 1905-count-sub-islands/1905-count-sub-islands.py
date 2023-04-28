class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #union find
        #change to graph datastructure
        #Union Find- Union() -- merges two graphs into one
        #           Find() -- finds the parent

        def in_bound(rw, cl, grid):
            m, n = len(grid), len(grid[0])
            return (0 <= rw < m) and (0 <= cl < n)

        def dfs(grid, visited, rw, cl):
            if not in_bound(rw, cl, grid):
                return 
            if (rw, cl) in visited or grid[rw][cl] == 0:
                return
            
            visited.add((rw, cl))
            grid[rw][cl] = 0
            dfs(grid, visited, rw+1, cl)
            dfs(grid, visited, rw-1, cl)
            dfs(grid, visited, rw, cl+1)
            dfs(grid, visited, rw, cl-1)
        
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
                    dfs(grid2, visited, i, j)
                    if isSubIsland(visited):
                        cnt += 1
        
        return cnt

