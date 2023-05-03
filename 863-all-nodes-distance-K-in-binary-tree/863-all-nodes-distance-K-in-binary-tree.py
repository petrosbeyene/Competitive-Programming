# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent, graph_dict):
            if not node:
                return
            if parent:
                graph_dict[node].append(parent)
                graph_dict[parent].append(node)
            dfs(node.left, node, graph_dict)
            dfs(node.right, node, graph_dict)
        
        graph_dict = defaultdict(list)
        dfs(root, None, graph_dict)
        
        if target not in graph_dict:
            return []
        
        ans = []
        bfs_q = deque([(target, 0)])
        visited = set([target])
        while bfs_q:
            node, dist = bfs_q.popleft()
            if dist == k:
                ans.append(node.val)
            elif dist < k:
                for neighbor in graph_dict[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        bfs_q.append((neighbor, dist+1))
        
        return ans
