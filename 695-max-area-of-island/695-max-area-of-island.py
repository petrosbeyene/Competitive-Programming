class Solution:
    def isValid(self, rw, cl, grid):
       return 0 <= rw < len(grid) and 0 <= cl < len(grid[0])

    def dfs(self, rw, cl, grid):
        if not self.isValid(rw, cl, grid) or grid[rw][cl] != 1:
            return 0
        
        grid[rw][cl] = 2
        ans_cnt = 1
        ans_cnt += self.dfs(rw+1, cl, grid)
        ans_cnt += self.dfs(rw-1, cl, grid)
        ans_cnt += self.dfs(rw, cl+1, grid)
        ans_cnt += self.dfs(rw, cl-1, grid)

        return ans_cnt

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_val = float('-inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = self.dfs(i, j, grid)
                    max_val = max(max_val, curr)

        return 0 if max_val == float('-inf') else max_val
