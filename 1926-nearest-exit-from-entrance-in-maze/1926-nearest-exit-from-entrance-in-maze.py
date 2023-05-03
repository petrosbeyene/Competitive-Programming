class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        
        queue = collections.deque()
        queue.appendleft([entrance[0],entrance[1],0])
    
        while queue:
            row, col, steps = queue.pop()
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.':
                    if (r == 0) or (c == 0) or (r == rows - 1) or (c == cols -1):
                        return steps+1 
                    
                    maze[r][c] = '+'
                    queue.appendleft([r,c,steps+1])

        return -1
