# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def bfs(currNode):

            if not currNode:
                return 0
            
            coins = bfs(currNode.left)
            coins2 = bfs(currNode.right)

            self.ans += abs(coins) + abs(coins2)

            coins = currNode.val + coins + coins2
            
            return coins - 1
        
        bfs(root)
        return self.ans
        
