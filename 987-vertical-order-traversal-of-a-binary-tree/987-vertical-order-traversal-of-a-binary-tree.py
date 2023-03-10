# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def extract(self, node, row, col):
        result = []
        if node:
            result += self.extract(node.left, row+1, col-1)
            result.append([col, row, node.val])
            result += self.extract(node.right, row+1, col+1)
        
        return result

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = self.extract(root, 0, 0)
        res.sort()
        
        new_res = []
        right = 0
        while right < len(res):
            temp = []
            while (right + 1 )< len(res) and res[right][0] == res[right+1][0]:
                temp.append(res[right])
                right += 1
            temp.append(res[right])
            right += 1

            new_res.append(temp)

        ans = []
        for i in new_res:
            temp = []
            for c, r, val in i: # here we are destructuring the list of list on the fly!
                temp.append(val)

            ans.append(temp)
        
        return ans
          
