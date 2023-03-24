# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        dic = {0:1}
        def preOrderTraversal(root, pref_sum):
            nonlocal ans
            if not root:
                return
            
            pref_sum += root.val         
            if pref_sum - targetSum in dic:
                ans += dic[pref_sum - targetSum]
            dic[pref_sum] = dic.get(pref_sum, 0) + 1
            
            #Left Pick
            preOrderTraversal(root.left, pref_sum)

            #Right Pick
            preOrderTraversal(root.right, pref_sum)
            dic[pref_sum] -= 1
        
        preOrderTraversal(root, 0)
        return ans
