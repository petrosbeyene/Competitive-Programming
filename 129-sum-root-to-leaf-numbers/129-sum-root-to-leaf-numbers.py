# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans_sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr_str):
            if not root:
                return
            
            curr_str += str(root.val)
            if not root.left and not root.right:
                self.ans_sum += int(curr_str)
                return
            
            dfs(root.left, curr_str)
            dfs(root.right, curr_str)
        
        dfs(root, "")

        return self.ans_sum
