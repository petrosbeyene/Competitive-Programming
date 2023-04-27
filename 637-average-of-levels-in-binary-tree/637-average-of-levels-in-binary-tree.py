# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        bfs_queue = deque()
        bfs_queue.append(root)

        averages = []
        while bfs_queue:
            curr_len = len(bfs_queue)
            curr_sum = 0
            for _ in range(curr_len):
                curr_node = bfs_queue.popleft()
                curr_sum += curr_node.val

                if curr_node.left:
                    bfs_queue.append(curr_node.left)
                if curr_node.right:
                    bfs_queue.append(curr_node.right)
            
            averages.append(curr_sum/curr_len)
        
        return averages
