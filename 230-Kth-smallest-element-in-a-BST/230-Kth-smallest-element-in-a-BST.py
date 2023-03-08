# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        if root:
            result += self.inorderTraversal(root.left)
            result.append(root.val)
            result += self.inorderTraversal(root.right)
        return result

    def kthSmallest(self, root: Optional[TreeNode], k: int, cnt=0) -> int:
        result = self.inorderTraversal(root)
        return result[k-1]
        
