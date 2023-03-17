# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt_sum = 0
        def backtrack(root):
            if not root: 
                return 0
            
            left_sum, right_sum = backtrack(root.left), backtrack(root.right)
            self.tilt_sum += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val
        
        backtrack(root)
        return self.tilt_sum
