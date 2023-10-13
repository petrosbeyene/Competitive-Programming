class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        
        left_next = {'N': 'W', 'E': 'N', 'W': 'S', 'S': 'E'}
        right_next = {'N': 'E', 'E': 'S', 'W': 'N', 'S': 'W'}

        curr_pos = [0, 0]
        curr_dir = 'N'
        for ins in instructions:
            if ins == 'G':
                curr_pos[0] += pos[curr_dir][0]
                curr_pos[1] += pos[curr_dir][1]
            elif ins == 'L':
                curr_dir = left_next[curr_dir]
            else:
                curr_dir = right_next[curr_dir]
    
        
        return (curr_pos == [0, 0] or curr_dir != 'N')

        
