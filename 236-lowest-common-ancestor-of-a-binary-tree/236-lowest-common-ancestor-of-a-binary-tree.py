# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_dic = {}
        
        def bfs(curr_node):
            if not curr_node:
                return
            
            if curr_node.left:
                parent_dic[curr_node.left] = curr_node
            if curr_node.right:
                parent_dic[curr_node.right] = curr_node
            
            bfs(curr_node.left)
            bfs(curr_node.right)
        
        bfs(root)

        # we will now backtrack to construct the parental hierarchy
        parents_for_p = [p]
        curr = p
        while curr in parent_dic:
            parents_for_p.append(parent_dic[curr])
            curr = parent_dic[curr]
        
        parents_for_q = [q]
        curr = q
        while curr in parent_dic:
            parents_for_q.append(parent_dic[curr])
            curr = parent_dic[curr]
        
        
        # Check if one is a parent of the other
        if p in set(parents_for_q):
            return p
        
        if q in set(parents_for_p):
            return q
        
        # Iterate and look for the parent, make the longer parents list a set
        for parent in parents_for_p:
            if parent in set(parents_for_q):
                return parent
        
        
