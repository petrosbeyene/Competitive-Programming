# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []
        path = []
        def backtrack(currNode, curr_sum):
            # print(path)
            if not currNode:
                return

            path.append(currNode.val)
            if curr_sum + currNode.val == targetSum and not currNode.left and not currNode.right:
                ans.append(path.copy())
                path.pop()
                return
            
            
            backtrack(currNode.left, curr_sum + currNode.val)

            backtrack(currNode.right, curr_sum + currNode.val)

            path.pop()


        backtrack(root, 0)
        return ans
        
