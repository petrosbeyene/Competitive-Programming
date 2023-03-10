# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        queue = [(root, 1)]
        answer = []

        while queue:
            temp = []
            curr_len = len(queue)
            while curr_len > 0:
                curr, idx = queue.pop(0)
                temp.append(idx)
                if curr.left:
                    queue.append((curr.left, 2*idx))
                if curr.right:
                    queue.append((curr.right, 2*idx+1))
                
                curr_len -= 1
            
            answer.append((temp[-1]-temp[0]+1))
        return max(answer)
        
