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

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = self.inorderTraversal(root)
        dic = Counter(result)

        highest_freq = max(dic.values())
        mode = filter(lambda x: dic[x]==highest_freq, dic.keys())

        return mode
