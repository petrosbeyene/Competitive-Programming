class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        eight_directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        bfs_queue = deque([(1, 0, 0)]) if grid[0][0] == 0 else deque()

        visited = set()
        while bfs_queue:
            dist, x, y = bfs_queue.popleft()
            if (x, y) == (n-1, n-1):
                return dist
            
            for dx, dy in eight_directions:
                if 0 <= x+dx < n and 0 <= y+dy < n and grid[x+dx][y+dy] == 0 and (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    bfs_queue.append((dist+1, x+dx, y+dy))
        
        return -1


