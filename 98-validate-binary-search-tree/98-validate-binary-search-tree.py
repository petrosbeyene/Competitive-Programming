# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], max_val=float('inf'), min_val=float('-inf')) -> bool:
        if not root:
            return True
        if not (root.val < max_val and root.val > min_val):
            return False
        
        return self.isValidBST(root.left, root.val, min_val) and self.isValidBST(root.right, max_val, root.val)
